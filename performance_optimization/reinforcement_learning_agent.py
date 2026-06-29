"""
OWLBAN GROUP - Reinforcement Learning Agent
With CPU (NumPy) and GPU (PyTorch) support
"""

import logging
import random

import numpy as np

# PyTorch imports - optional, with NumPy fallback
try:
    import torch
    import torch.nn as nn
    import torch.optim as optim

    TORCH_AVAILABLE = True
except ImportError:
    torch = None  # type: ignore
    nn = None  # type: ignore
    optim = None  # type: ignore
    TORCH_AVAILABLE = False


# Factory function to create DQN network - avoids class redefinition issue
def _create_optimized_dqn(state_size, action_size, hidden_size=128):
    """Factory function to create appropriate DQN network based on availability.

    Args:
        state_size: Size of the state space
        action_size: Size of the action space
        hidden_size: Size of hidden layers

    Returns:
        An OptimizedDQNNetwork instance (GPU or CPU fallback)
    """
    if TORCH_AVAILABLE:
        # NVIDIA GPU-accelerated version with cuDNN
        class OptimizedDQNNetwork(nn.Module):
            """NVIDIA-optimized Deep Q-Network with cuDNN acceleration"""
            def __init__(self, state_sz, action_sz, hidden_sz=128):
                super(OptimizedDQNNetwork, self).__init__()
                self.layers = nn.Sequential(
                    nn.Linear(state_sz, hidden_sz),
                    nn.ReLU(),
                    nn.Dropout(0.1),
                    nn.Linear(hidden_sz, hidden_sz),
                    nn.ReLU(),
                    nn.Dropout(0.1),
                    nn.Linear(hidden_sz, action_sz)
)

            def forward(self, x):
                """Forward pass through the Q-network.

                Args:
                    x: Input tensor of shape (batch_size, state_size)

                Returns:
                    Q-values for each action of shape (batch_size, action_size)
                """
                return self.layers(x)

        return OptimizedDQNNetwork(state_size, action_size, hidden_size)
    else:
        # pylint: disable=too-few-public-methods
        # CPU fallback version when PyTorch not available
        class OptimizedDQNNetwork:
            """Fallback DQN network when PyTorch is not available"""
            def __init__(self, state_sz, action_sz, hidden_sz=128):
                self.state_size = state_sz
                self.action_size = action_sz
                self.hidden_size = hidden_sz

            def __call__(self, x):
                """Return dummy Q-values"""
                return np.zeros(
                    (x.shape[0] if hasattr(x, "shape") else 1),
                    self.action_size
                )

        return OptimizedDQNNetwork(state_size, action_size, hidden_size)


class NumPyQLearningAgent:
    """NumPy-based Q-Learning agent for CPU fallback"""
    def __init__(self, actions, learning_rate=0.1, discount_factor=0.99,
                 epsilon=0.2, epsilon_decay=0.995, epsilon_min=0.01):
        self.actions = actions
        self.action_size = len(actions)
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min

        # Q-table for state-action values
        self.q_table = {}

    def get_state_key(self, state):
        """Convert state to discretized string key for Q-table"""
        if isinstance(state, (np.ndarray, list, tuple)):
            # Discretize state to reduce table size
            discretized = tuple(int(s * 10) for s in state)
            return str(discretized)
        return str(state)

    def choose_action(self, state):
        """Epsilon-greedy action selection"""
        if random.random() < self.epsilon:
            return random.choice(self.actions)

        # Get Q-values for this state
        state_key = self.get_state_key(state)
        if state_key not in self.q_table:
            self.q_table[state_key] = {a: 0.0 for a in self.actions}

        # Choose best action
        q_values = self.q_table[state_key]
        return max(q_values, key=q_values.get)

    def learn(self, state, action, reward, next_state):
        """Update Q-value using Q-learning"""
        state_key = self.get_state_key(state)
        next_state_key = self.get_state_key(next_state)

        # Initialize if needed
        if state_key not in self.q_table:
            self.q_table[state_key] = {a: 0.0 for a in self.actions}
        if next_state_key not in self.q_table:
            self.q_table[next_state_key] = {a: 0.0 for a in self.actions}

        # Q-learning update
        current_q = self.q_table[state_key][action]
        max_next_q = max(self.q_table[next_state_key].values())
        target = reward + self.discount_factor * max_next_q
        self.q_table[state_key][action] += self.learning_rate * (target - current_q)

        # Decay epsilon
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def reset_parameters(self, learning_rate=None, discount_factor=None, epsilon=None):
        """Reset parameters"""
        if learning_rate is not None:
            self.learning_rate = learning_rate
        if discount_factor is not None:
            self.discount_factor = discount_factor
        if epsilon is not None:
            self.epsilon = epsilon

    def get_gpu_status(self):
        """Get GPU status"""
        return {
            "device": "numpy_cpu",
            "cuda_available": False,
            "memory_allocated": 0,
            "memory_reserved": 0,
            "q_table_size": len(self.q_table)
        }


class ReinforcementLearningAgent:
    """Reinforcement Learning agent with CPU (NumPy) and GPU (PyTorch) support"""
    def __init__(self, actions, learning_rate=0.001, discount_factor=0.99, epsilon=0.2,
                 epsilon_decay=0.995, epsilon_min=0.01, use_gpu=True):
        self.actions = actions
        self.action_size = len(actions)
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min

        self.logger = logging.getLogger("RLAgent")

        # Determine device and use appropriate backend
        self.use_torch = TORCH_AVAILABLE and use_gpu and torch.cuda.is_available()

        if self.use_torch:
            # Use PyTorch GPU backend
            self.device = torch.device("cuda")
            self.logger.info("NVIDIA GPU-accelerated RL using device: %s", self.device)

            # Initialize Deep Q-Network for GPU acceleration
            self.state_size = 10  # Default, will be updated dynamically
            self.dqn = _create_optimized_dqn(
                self.state_size, self.action_size
            ).to(self.device)
            self.target_dqn = _create_optimized_dqn(
                self.state_size, self.action_size
            ).to(self.device)
            self.target_dqn.load_state_dict(self.dqn.state_dict())

            # Enable cuDNN optimization
            torch.backends.cudnn.benchmark = True

            self.optimizer = optim.Adam(self.dqn.parameters(), lr=learning_rate)
            self.criterion = nn.MSELoss()

        else:
            # Use NumPy CPU fallback
            self.device = "numpy_cpu"
            self.logger.info("Using NumPy CPU-based Q-Learning (PyTorch not available)")

            # Initialize NumPy Q-Learning agent as fallback
            self.numpy_agent = NumPyQLearningAgent(
                actions=actions,
                learning_rate=0.1,  # Higher LR for tabular learning
                discount_factor=discount_factor,
                epsilon=epsilon,
                epsilon_decay=epsilon_decay,
                epsilon_min=epsilon_min
            )

        # Experience replay buffer (for both backends)
        self.memory = []
        self.memory_size = 10000
        self.batch_size = 64

        self.update_target_every = 100
        self.step_count = 0

    def get_state_key(self, state):
        """Convert state to string key for Q-table"""
        if isinstance(state, (np.ndarray, list, tuple)):
            return str(tuple(state))
        return str(state)

    def _convert_state_to_numeric(self, state):
        """Convert state to numeric list"""
        if isinstance(state, (list, tuple)):
            numeric_state = []
            for s in state:
                if isinstance(s, (int, float)):
                    numeric_state.append(float(s))
                elif isinstance(s, str):
                    numeric_state.append(hash(s) % 1000 / 1000.0)
                elif isinstance(s, bool):
                    numeric_state.append(1.0 if s else 0.0)
                else:
                    numeric_state.append(0.0)
            return numeric_state
        return state

    def choose_action(self, state):
        """Choose action using appropriate backend"""
        state = self._convert_state_to_numeric(state)

        if self.use_torch:
            # PyTorch GPU path
            if isinstance(state, (list, tuple)):
                state_tensor = torch.tensor(
                    state, dtype=torch.float32
                ).unsqueeze(0).to(self.device)
            else:
                state_tensor = state.unsqueeze(0).to(self.device) if hasattr(
                    state, 'unsqueeze'
                ) else state

            # Epsilon-greedy exploration
            if random.random() < self.epsilon:
                return random.choice(self.actions)

            with torch.no_grad():
                q_values = self.dqn(state_tensor)
                action_idx = torch.argmax(q_values).item()

            return self.actions[action_idx]
        else:
            # NumPy CPU path
            return self.numpy_agent.choose_action(state)

    def learn(self, state, action, reward, next_state):
        """Learn using appropriate backend"""
        state = self._convert_state_to_numeric(state)
        next_state = self._convert_state_to_numeric(next_state)

        if self.use_torch:
            # PyTorch GPU learning
            self.memory.append(
                (state, self.actions.index(action), reward, next_state)
            )
            if len(self.memory) > self.memory_size:
                self.memory.pop(0)

            # Train DQN if enough experiences
            if len(self.memory) >= self.batch_size:
                self._train_dqn()

            # Update target network periodically
            self.step_count += 1
            if self.step_count % self.update_target_every == 0:
                self.target_dqn.load_state_dict(self.dqn.state_dict())
        else:
            # NumPy CPU learning
            self.numpy_agent.learn(state, action, reward, next_state)

        # Decay epsilon
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def _train_dqn(self):
        """Train DQN using NVIDIA GPU acceleration"""
        # Sample batch from memory
        batch = random.sample(self.memory, self.batch_size)
        states, actions, rewards, next_states = zip(*batch)

        # Convert to tensors
        states = torch.tensor(states, dtype=torch.float32).to(self.device)
        actions = torch.tensor(actions, dtype=torch.long).to(self.device)
        rewards = torch.tensor(rewards, dtype=torch.float32).to(self.device)
        next_states = torch.tensor(next_states, dtype=torch.float32).to(self.device)

        # Current Q values
        current_q = self.dqn(states).gather(1, actions.unsqueeze(1)).squeeze(1)

        # Target Q values
        with torch.no_grad():
            next_q = self.target_dqn(next_states).max(1)[0]
            target_q = rewards + self.discount_factor * next_q

        # Compute loss and update
        loss = self.criterion(current_q, target_q)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

    def reset_parameters(self, learning_rate=None, discount_factor=None, epsilon=None):
        """Reset parameters"""
        if learning_rate is not None:
            self.learning_rate = learning_rate
        if discount_factor is not None:
            self.discount_factor = discount_factor
        if epsilon is not None:
            self.epsilon = epsilon

        if not self.use_torch and hasattr(self, 'numpy_agent'):
            self.numpy_agent.reset_parameters(
                learning_rate, discount_factor, epsilon
            )

    def get_gpu_status(self):
        """Get NVIDIA GPU status for RL training"""
        if self.use_torch:
            cuda_avail = torch.cuda.is_available()
            return {
                "device": str(self.device),
                "cuda_available": cuda_avail,
                "memory_allocated": torch.cuda.memory_allocated(
                    self.device
                ) / 1024**3 if cuda_avail else 0,
                "memory_reserved": torch.cuda.memory_reserved(
                    self.device
                ) / 1024**3 if cuda_avail else 0,
                "experience_buffer_size": len(self.memory)
            }
        else:
            return {
                "device": "numpy_cpu",
                "cuda_available": False,
                "memory_allocated": 0,
                "memory_reserved": 0,
                "experience_buffer_size": len(self.memory)
            }
