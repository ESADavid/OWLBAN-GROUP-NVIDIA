"""
OWLBAN GROUP AI Database Manager
Unified database interface for all AI systems with SQL and NoSQL support
"""

import sqlite3
import json
import logging
from typing import Any, Dict, List, Optional
from datetime import datetime

# Optional database drivers
try:
    import pymongo
    from pymongo import MongoClient
    MONGODB_AVAILABLE = True
except ImportError:
    MONGODB_AVAILABLE = False

try:
    import psycopg2
    POSTGRESQL_AVAILABLE = True
except ImportError:
    POSTGRESQL_AVAILABLE = False

try:
    import redis
    REDIS_AVAILABLE = True
except ImportError:
    REDIS_AVAILABLE = False

class DatabaseManager:
    """Unified database manager supporting multiple database types"""

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.logger = logging.getLogger("DatabaseManager")
        self.config = config or self._default_config()
self.connections: Dict[str, Any] = {}

        # Initialize databases
        self._init_sqlite()
        if MONGODB_AVAILABLE:
            self._init_mongodb()
        if POSTGRESQL_AVAILABLE:
            self._init_postgresql()
        if REDIS_AVAILABLE:
            self._init_redis()

    def _default_config(self) -> Dict[str, Any]:
        return {
            "sqlite": {
                "path": "owlban_ai.db"
            },
            "mongodb": {
                "host": "localhost",
                "port": 27017,
                "database": "owlban_ai"
            },
            "postgresql": {
                "host": "localhost",
                "port": 5432,
                "database": "owlban_ai",
                "user": "owlban",
                "password": "password"
            },
            "redis": {
                "host": "localhost",
                "port": 6379,
                "db": 0
            }
        }

    def _init_sqlite(self):
        """Initialize SQLite database"""
        try:
            db_path = self.config["sqlite"]["path"]
            self.connections["sqlite"] = sqlite3.connect(db_path)
            self._create_sqlite_tables()
            self.logger.info("SQLite database initialized")
        except sqlite3.Error as e:
            self.logger.error("SQLite initialization failed: %s", e)

    def _create_sqlite_tables(self):
        """Create necessary SQLite tables"""
        cursor = self.connections["sqlite"].cursor()

        # AI predictions table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS predictions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                model_name TEXT NOT NULL,
                input_data TEXT,
                prediction TEXT,
                confidence REAL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Revenue optimization results
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS revenue_optimization (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                strategy TEXT,
                profit REAL,
                parameters TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # System metrics
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS system_metrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                metric_name TEXT,
                value REAL,
                tags TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')

# Quantum computations
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS quantum_computations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                algorithm TEXT,
                input_parameters TEXT,
                result TEXT,
                execution_time REAL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Employees table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                employee_id TEXT UNIQUE NOT NULL,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                phone TEXT,
                position TEXT,
                department TEXT,
                salary REAL,
                hire_date TEXT,
                employment_status TEXT DEFAULT 'active',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Employee Benefits table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS employee_benefits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                employee_id TEXT UNIQUE NOT NULL,
                health_insurance_plan TEXT,
                health_insurance_provider TEXT,
                health_insurance_start_date TEXT,
                health_insurance_premium REAL,
                health_insurance_coverage_type TEXT,
                life_insurance_status TEXT DEFAULT 'not_enrolled',
                life_insurance_amount REAL,
                life_insurance_provider TEXT,
                life_insurance_premium REAL,
                life_insurance_beneficiary TEXT,
                k401_enrolled INTEGER DEFAULT 0,
                k401_contribution_percentage REAL,
                k401_employer_match_percentage REAL,
                k401_start_date TEXT,
                k401_current_balance REAL,
                benefits_notes TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Payroll table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS payroll (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                payroll_id TEXT UNIQUE NOT NULL,
                employee_id TEXT,
                pay_period_start TEXT NOT NULL,
                pay_period_end TEXT NOT NULL,
                pay_date TEXT NOT NULL,
                base_salary REAL,
                overtime_pay REAL,
                bonuses REAL,
                commissions REAL,
                federal_tax_withholding REAL,
                state_tax_withholding REAL,
                social_security_tax REAL,
                medicare_tax REAL,
                health_insurance_premium REAL,
                life_insurance_premium REAL,
                k401_contribution REAL,
                other_deductions REAL,
                gross_pay REAL,
                net_pay REAL,
                payment_status TEXT DEFAULT 'pending',
                payment_method TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Benefits Enrollment History
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS benefits_enrollment_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                employee_id TEXT,
                benefit_type TEXT NOT NULL,
                action TEXT NOT NULL,
                previous_value TEXT,
                new_value TEXT,
                effective_date TEXT,
                performed_by TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        self.connections["sqlite"].commit()

    def _init_mongodb(self):
        """Initialize MongoDB connection"""
        try:
            config = self.config["mongodb"]
            client = MongoClient(config["host"], config["port"])
            self.connections["mongodb"] = client[config["database"]]
            self.logger.info("MongoDB connection initialized")
        except Exception as e:
            self.logger.error(f"MongoDB initialization failed: {e}")

    def _init_postgresql(self):
        """Initialize PostgreSQL connection"""
        try:
            config = self.config["postgresql"]
            conn_string = f"host={config['host']} port={config['port']} dbname={config['database']} user={config['user']} password={config['password']}"
            self.connections["postgresql"] = psycopg2.connect(conn_string)
            self._create_postgresql_tables()
            self.logger.info("PostgreSQL connection initialized")
        except Exception as e:
            self.logger.error(f"PostgreSQL initialization failed: {e}")

    def _create_postgresql_tables(self):
        """Create PostgreSQL tables if they don't exist"""
        cursor = self.connections["postgresql"].cursor()

        # Similar table structure as SQLite but for PostgreSQL
        tables = [
            """
            CREATE TABLE IF NOT EXISTS predictions (
                id SERIAL PRIMARY KEY,
                model_name VARCHAR(255) NOT NULL,
                input_data JSONB,
                prediction JSONB,
                confidence DOUBLE PRECISION,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS revenue_optimization (
                id SERIAL PRIMARY KEY,
                strategy VARCHAR(255),
                profit DOUBLE PRECISION,
                parameters JSONB,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS system_metrics (
                id SERIAL PRIMARY KEY,
                metric_name VARCHAR(255),
                value DOUBLE PRECISION,
                tags JSONB,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        ]

        for table_sql in tables:
            try:
                cursor.execute(table_sql)
            except Exception as e:
                self.logger.warning(f"Table creation failed: {e}")

        self.connections["postgresql"].commit()
        cursor.close()

    def _init_redis(self):
        """Initialize Redis connection"""
        try:
            config = self.config["redis"]
            self.connections["redis"] = redis.Redis(
                host=config["host"],
                port=config["port"],
                db=config["db"]
            )
            self.logger.info("Redis connection initialized")
        except Exception as e:
            self.logger.error(f"Redis initialization failed: {e}")

    # SQLite operations
    def save_prediction_sqlite(self, model_name: str, input_data: Dict, prediction: Any, confidence: float):
        """Save prediction to SQLite"""
        if "sqlite" not in self.connections:
            return False

        try:
            cursor = self.connections["sqlite"].cursor()
            cursor.execute(
                "INSERT INTO predictions (model_name, input_data, prediction, confidence) VALUES (?, ?, ?, ?)",
                (model_name, json.dumps(input_data), json.dumps(prediction), confidence)
            )
            self.connections["sqlite"].commit()
            return True
        except Exception as e:
            self.logger.error(f"SQLite save prediction failed: {e}")
            return False

    def get_predictions_sqlite(self, model_name: Optional[str] = None, limit: int = 100) -> List[Dict]:
        """Get predictions from SQLite"""
        if "sqlite" not in self.connections:
            return []

        try:
            cursor = self.connections["sqlite"].cursor()
            if model_name:
                cursor.execute(
                    "SELECT * FROM predictions WHERE model_name = ? ORDER BY timestamp DESC LIMIT ?",
                    (model_name, limit)
                )
            else:
                cursor.execute("SELECT * FROM predictions ORDER BY timestamp DESC LIMIT ?", (limit,))

            columns = [desc[0] for desc in cursor.description]
            results = []
            for row in cursor.fetchall():
                result = dict(zip(columns, row))
                # Parse JSON fields
                if result.get('input_data'):
                    result['input_data'] = json.loads(result['input_data'])
                if result.get('prediction'):
                    result['prediction'] = json.loads(result['prediction'])
                results.append(result)

            return results
        except Exception as e:
            self.logger.error(f"SQLite get predictions failed: {e}")
            return []

    # MongoDB operations
    def save_prediction_mongodb(self, model_name: str, input_data: Dict, prediction: Any, confidence: float):
        """Save prediction to MongoDB"""
        if "mongodb" not in self.connections:
            return False

        try:
            collection = self.connections["mongodb"].predictions
            doc = {
                "model_name": model_name,
                "input_data": input_data,
                "prediction": prediction,
                "confidence": confidence,
                "timestamp": datetime.utcnow()
            }
            collection.insert_one(doc)
            return True
        except Exception as e:
            self.logger.error(f"MongoDB save prediction failed: {e}")
            return False

    # Redis operations
    def cache_prediction_redis(self, key: str, prediction: Dict, ttl: int = 3600):
        """Cache prediction in Redis"""
        if "redis" not in self.connections:
            return False

        try:
            self.connections["redis"].setex(key, ttl, json.dumps(prediction))
            return True
        except Exception as e:
            self.logger.error(f"Redis cache prediction failed: {e}")
            return False

    def get_cached_prediction_redis(self, key: str) -> Optional[Dict]:
        """Get cached prediction from Redis"""
        if "redis" not in self.connections:
            return None

        try:
            data = self.connections["redis"].get(key)
            if data:
                return json.loads(data)
            return None
        except Exception as e:
            self.logger.error(f"Redis get cached prediction failed: {e}")
            return None

    # Unified interface
    def save_prediction(self, model_name: str, input_data: Dict, prediction: Any, confidence: float):
        """Save prediction to all available databases"""
        results = []

        # Save to SQLite
        results.append(("sqlite", self.save_prediction_sqlite(model_name, input_data, prediction, confidence)))

# Save to MongoDB if available
        if MONGODB_AVAILABLE:
            results.append(("mongodb", self.save_prediction_mongodb(model_name, input_data, prediction, confidence)))

        # Cache in Redis if available
        if REDIS_AVAILABLE:
            cache_key = f"prediction:{model_name}:{hash(str(input_data))}"
            cache_data = {
                "model_name": model_name,
                "input_data": input_data,
                "prediction": prediction,
                "confidence": confidence,
                "timestamp": datetime.utcnow().isoformat()
            }
            results.append(("redis", self.cache_prediction_redis(cache_key, cache_data)))

        return results

    def get_predictions(self, model_name: Optional[str] = None, limit: int = 100) -> List[Dict]:
        """Get predictions from primary database (SQLite)"""
        return self.get_predictions_sqlite(model_name, limit)

    def save_revenue_result(self, strategy: str, profit: float, parameters: Dict):
        """Save revenue optimization result"""
        if "sqlite" not in self.connections:
            return False

        try:
            cursor = self.connections["sqlite"].cursor()
            cursor.execute(
                "INSERT INTO revenue_optimization (strategy, profit, parameters) VALUES (?, ?, ?)",
                (strategy, profit, json.dumps(parameters))
            )
            self.connections["sqlite"].commit()
            return True
        except Exception as e:
            self.logger.error(f"Save revenue result failed: {e}")
            return False

    def save_system_metric(self, metric_name: str, value: float, tags: Optional[Dict] = None):
        """Save system metric"""
        if "sqlite" not in self.connections:
            return False

        try:
            cursor = self.connections["sqlite"].cursor()
            cursor.execute(
                "INSERT INTO system_metrics (metric_name, value, tags) VALUES (?, ?, ?)",
                (metric_name, value, json.dumps(tags or {}))
            )
            self.connections["sqlite"].commit()
            return True
        except Exception as e:
            self.logger.error(f"Save system metric failed: {e}")
            return False

    def save_quantum_computation(self, algorithm: str, input_parameters: Dict, result: Any, execution_time: float):
        """Save quantum computation result"""
        if "sqlite" not in self.connections:
            return False

        try:
            cursor = self.connections["sqlite"].cursor()
            cursor.execute(
                "INSERT INTO quantum_computations (algorithm, input_parameters, result, execution_time) VALUES (?, ?, ?, ?)",
                (algorithm, json.dumps(input_parameters), json.dumps(result), execution_time)
            )
            self.connections["sqlite"].commit()
            return True
        except Exception as e:
            self.logger.error(f"Save quantum computation failed: {e}")
            return False

    def get_database_status(self) -> Dict[str, Any]:
        """Get status of all database connections"""
        status = {}
        for db_type, connection in self.connections.items():
            try:
                if db_type == "sqlite":
                    cursor = connection.cursor()
                    cursor.execute("SELECT COUNT(*) FROM predictions")
                    count = cursor.fetchone()[0]
                    status[db_type] = {"connected": True, "predictions_count": count}
                elif db_type == "mongodb":
                    status[db_type] = {"connected": True, "collections": connection.list_collection_names()}
                elif db_type == "postgresql":
                    cursor = connection.cursor()
                    cursor.execute("SELECT COUNT(*) FROM predictions")
                    count = cursor.fetchone()[0]
                    status[db_type] = {"connected": True, "predictions_count": count}
                    cursor.close()
                elif db_type == "redis":
                    status[db_type] = {"connected": connection.ping(), "db": connection.connection.db}
            except Exception as e:
                status[db_type] = {"connected": False, "error": str(e)}

        return status

# =============================================================================
    # Employee Management Methods
    # =============================================================================

    def add_employee(self, employee_id: str, first_name: str, last_name: str, email: str,
                     phone: Optional[str] = None, position: Optional[str] = None,
                     department: Optional[str] = None, salary: Optional[float] = None,
                     hire_date: Optional[str] = None) -> bool:
        """Add a new employee to the database"""
        if "sqlite" not in self.connections:
            return False

        try:
            cursor = self.connections["sqlite"].cursor()
            cursor.execute(
                """INSERT INTO employees (employee_id, first_name, last_name, email, phone, position, department, salary, hire_date)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (employee_id, first_name, last_name, email, phone, position, department, salary, hire_date)
            )
            self.connections["sqlite"].commit()
            return True
        except Exception as e:
            self.logger.error(f"Add employee failed: {e}")
            return False

    def get_employee(self, employee_id: str) -> Optional[Dict]:
        """Get employee by employee_id"""
        if "sqlite" not in self.connections:
            return None

        try:
            cursor = self.connections["sqlite"].cursor()
            cursor.execute("SELECT * FROM employees WHERE employee_id = ?", (employee_id,))
            row = cursor.fetchone()
            if row:
                columns = [desc[0] for desc in cursor.description]
                return dict(zip(columns, row))
            return None
        except Exception as e:
            self.logger.error(f"Get employee failed: {e}")
            return None

    def get_all_employees(self, department: Optional[str] = None, status: Optional[str] = None, limit: int = 100) -> List[Dict]:
        """Get all employees with optional filters"""
        if "sqlite" not in self.connections:
            return []

        try:
            cursor = self.connections["sqlite"].cursor()
            query = "SELECT * FROM employees WHERE 1=1"
            params = []

            if department:
                query += " AND department = ?"
                params.append(department)
            if status:
                query += " AND employment_status = ?"
                params.append(status)

            query += f" LIMIT {limit}"
            cursor.execute(query, params)

            columns = [desc[0] for desc in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]
            return results
        except Exception as e:
            self.logger.error(f"Get all employees failed: {e}")
            return []

    def update_employee(self, employee_id: str, **kwargs) -> bool:
        """Update employee information"""
        if "sqlite" not in self.connections:
            return False

        try:
            cursor = self.connections["sqlite"].cursor()
            set_clause = ", ".join([f"{key} = ?" for key in kwargs.keys()])
            values = list(kwargs.values())
            values.append(employee_id)

            cursor.execute(
                f"UPDATE employees SET {set_clause}, updated_at = CURRENT_TIMESTAMP WHERE employee_id = ?",
                values
            )
            self.connections["sqlite"].commit()
            return cursor.rowcount > 0
        except Exception as e:
            self.logger.error(f"Update employee failed: {e}")
            return False

    def delete_employee(self, employee_id: str) -> bool:
        """Delete an employee"""
        if "sqlite" not in self.connections:
            return False

        try:
            cursor = self.connections["sqlite"].cursor()
            cursor.execute("DELETE FROM employees WHERE employee_id = ?", (employee_id,))
            self.connections["sqlite"].commit()
            return cursor.rowcount > 0
        except Exception as e:
            self.logger.error(f"Delete employee failed: {e}")
            return False

# =============================================================================
    # Employee Benefits Management Methods
    # =============================================================================

    def add_employee_benefits(self, employee_id: str, health_insurance_plan: Optional[str] = None,
                             health_insurance_provider: Optional[str] = None,
                             health_insurance_premium: Optional[float] = None,
health_insurance_coverage_type: Optional[str] = None,
                             life_insurance_status: str = "not_enrolled",
                             life_insurance_amount: Optional[float] = None,
                             life_insurance_provider: Optional[str] = None,
                             life_insurance_premium: Optional[float] = None,
                             life_insurance_beneficiary: Optional[str] = None,
                             k401_enrolled: bool = False,
                             k401_contribution_percentage: Optional[float] = None,
                             k401_employer_match_percentage: Optional[float] = None) -> bool:
        """Add or update employee benefits"""
        if "sqlite" not in self.connections:
            return False

        try:
            cursor = self.connections["sqlite"].cursor()
            cursor.execute(
                """INSERT OR REPLACE INTO employee_benefits 
                   (employee_id, health_insurance_plan, health_insurance_provider, health_insurance_premium,
                    health_insurance_coverage_type, life_insurance_status, life_insurance_amount, life_insurance_provider,
                    life_insurance_premium, life_insurance_beneficiary, k401_enrolled, k401_contribution_percentage,
                    k401_employer_match_percentage)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (employee_id, health_insurance_plan, health_insurance_provider, health_insurance_premium,
                 health_insurance_coverage_type, life_insurance_status, life_insurance_amount, life_insurance_provider,
                 life_insurance_premium, life_insurance_beneficiary, 1 if k401_enrolled else 0,
                 k401_contribution_percentage, k401_employer_match_percentage)
            )
            self.connections["sqlite"].commit()
            return True
        except Exception as e:
            self.logger.error(f"Add employee benefits failed: {e}")
            return False

    def get_employee_benefits(self, employee_id: str) -> Optional[Dict]:
        """Get employee benefits by employee_id"""
        if "sqlite" not in self.connections:
            return None

        try:
            cursor = self.connections["sqlite"].cursor()
            cursor.execute("SELECT * FROM employee_benefits WHERE employee_id = ?", (employee_id,))
            row = cursor.fetchone()
            if row:
                columns = [desc[0] for desc in cursor.description]
                result = dict(zip(columns, row))
                # Convert k401_enrolled from integer to boolean
                result['k401_enrolled'] = bool(result.get('k401_enrolled'))
                return result
            return None
        except Exception as e:
            self.logger.error(f"Get employee benefits failed: {e}")
            return None

    def get_all_employees_benefits(self, k401_enrolled: Optional[bool] = None) -> List[Dict]:
        """Get all employees with benefits information"""
        if "sqlite" not in self.connections:
            return []

        try:
            cursor = self.connections["sqlite"].cursor()
            query = "SELECT * FROM employee_benefits WHERE 1=1"
            params = []

            if k401_enrolled is not None:
                query += " AND k401_enrolled = ?"
                params.append(1 if k401_enrolled else 0)

            cursor.execute(query, params)

            columns = [desc[0] for desc in cursor.description]
            results = []
            for row in cursor.fetchall():
                result = dict(zip(columns, row))
                result['k401_enrolled'] = bool(result.get('k401_enrolled'))
                results.append(result)
            return results
        except Exception as e:
            self.logger.error(f"Get all employee benefits failed: {e}")
            return []

    def update_employee_benefits(self, employee_id: str, **kwargs) -> bool:
        """Update employee benefits"""
        if "sqlite" not in self.connections:
            return False

        try:
            cursor = self.connections["sqlite"].cursor()
            set_clause = ", ".join([f"{key} = ?" for key in kwargs.keys()])
            values = list(kwargs.values())
            values.append(employee_id)

            cursor.execute(
                f"UPDATE employee_benefits SET {set_clause}, updated_at = CURRENT_TIMESTAMP WHERE employee_id = ?",
                values
            )
            self.connections["sqlite"].commit()
            return cursor.rowcount > 0
        except Exception as e:
            self.logger.error(f"Update employee benefits failed: {e}")
            return False

    def record_benefits_enrollment_history(self, employee_id: str, benefit_type: str, action: str,
                                           previous_value: Optional[str] = None,
                                           new_value: Optional[str] = None,
                                           effective_date: Optional[str] = None,
                                           performed_by: Optional[str] = None) -> bool:
        """Record benefits enrollment history"""
        if "sqlite" not in self.connections:
            return False

        try:
            cursor = self.connections["sqlite"].cursor()
            cursor.execute(
                """INSERT INTO benefits_enrollment_history 
                   (employee_id, benefit_type, action, previous_value, new_value, effective_date, performed_by)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (employee_id, benefit_type, action, previous_value, new_value, effective_date, performed_by)
            )
            self.connections["sqlite"].commit()
            return True
        except Exception as e:
            self.logger.error(f"Record benefits enrollment history failed: {e}")
            return False

    # =============================================================================
    # Payroll Management Methods
    # =============================================================================

    def process_payroll(self, payroll_id: str, employee_id: str, pay_period_start: str, pay_period_end: str,
                        pay_date: str, base_salary: float, overtime_pay: float = 0, bonuses: float = 0,
                        commissions: float = 0, federal_tax_rate: float = 0.22, state_tax_rate: float = 0.05,
                        social_security_rate: float = 0.062, medicare_rate: float = 0.0145,
                        health_insurance_premium: float = 0, life_insurance_premium: float = 0,
                        k401_contribution: float = 0, other_deductions: float = 0,
                        payment_method: str = "direct_deposit") -> Optional[Dict]:
        """Process payroll for an employee"""
        if "sqlite" not in self.connections:
            return None

        try:
            # Calculate gross pay
            gross_pay = base_salary + overtime_pay + bonuses + commissions

            # Calculate taxes and deductions
            federal_tax_withholding = gross_pay * federal_tax_rate
            state_tax_withholding = gross_pay * state_tax_rate
            social_security_tax = gross_pay * social_security_rate
            medicare_tax = gross_pay * medicare_rate

            # Calculate net pay
            total_deductions = (federal_tax_withholding + state_tax_withholding +
                              social_security_tax + medicare_tax +
                              health_insurance_premium + life_insurance_premium +
                              k401_contribution + other_deductions)
            net_pay = gross_pay - total_deductions

            cursor = self.connections["sqlite"].cursor()
            cursor.execute(
                """INSERT INTO payroll 
                   (payroll_id, employee_id, pay_period_start, pay_period_end, pay_date, base_salary,
                    overtime_pay, bonuses, commissions, federal_tax_withholding, state_tax_withholding,
                    social_security_tax, medicare_tax, health_insurance_premium, life_insurance_premium,
                    k401_contribution, other_deductions, gross_pay, net_pay, payment_status, payment_method)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'pending', ?)""",
                (payroll_id, employee_id, pay_period_start, pay_period_end, pay_date, base_salary,
                 overtime_pay, bonuses, commissions, federal_tax_withholding, state_tax_withholding,
                 social_security_tax, medicare_tax, health_insurance_premium, life_insurance_premium,
                 k401_contribution, other_deductions, gross_pay, net_pay, payment_method)
            )
            self.connections["sqlite"].commit()

            return {
                "payroll_id": payroll_id,
                "employee_id": employee_id,
                "gross_pay": gross_pay,
                "net_pay": net_pay,
                "total_deductions": total_deductions,
                "payment_status": "pending"
            }
        except Exception as e:
            self.logger.error(f"Process payroll failed: {e}")
            return None

    def get_payroll(self, employee_id: str, limit: int = 12) -> List[Dict]:
        """Get payroll history for an employee"""
        if "sqlite" not in self.connections:
            return []

        try:
            cursor = self.connections["sqlite"].cursor()
            cursor.execute(
                "SELECT * FROM payroll WHERE employee_id = ? ORDER BY pay_period_end DESC LIMIT ?",
                (employee_id, limit)
            )

            columns = [desc[0] for desc in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]
            return results
        except Exception as e:
            self.logger.error(f"Get payroll failed: {e}")
            return []

    def get_payroll_by_id(self, payroll_id: str) -> Optional[Dict]:
        """Get specific payroll record"""
        if "sqlite" not in self.connections:
            return None

        try:
            cursor = self.connections["sqlite"].cursor()
            cursor.execute("SELECT * FROM payroll WHERE payroll_id = ?", (payroll_id,))
            row = cursor.fetchone()
            if row:
                columns = [desc[0] for desc in cursor.description]
                return dict(zip(columns, row))
            return None
        except Exception as e:
            self.logger.error(f"Get payroll by ID failed: {e}")
            return None

    def update_payroll_status(self, payroll_id: str, status: str) -> bool:
        """Update payroll payment status"""
        if "sqlite" not in self.connections:
            return False

        try:
            cursor = self.connections["sqlite"].cursor()
            cursor.execute(
                "UPDATE payroll SET payment_status = ? WHERE payroll_id = ?",
                (status, payroll_id)
            )
            self.connections["sqlite"].commit()
            return cursor.rowcount > 0
        except Exception as e:
            self.logger.error(f"Update payroll status failed: {e}")
            return False

    def get_all_payroll(self, status: Optional[str] = None, limit: int = 100) -> List[Dict]:
        """Get all payroll records"""
        if "sqlite" not in self.connections:
            return []

        try:
            cursor = self.connections["sqlite"].cursor()
            query = "SELECT * FROM payroll"
            params = []

            if status:
                query += " WHERE payment_status = ?"
                params.append(status)

            query += f" ORDER BY pay_period_end DESC LIMIT {limit}"
            cursor.execute(query, params)

            columns = [desc[0] for desc in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]
            return results
        except Exception as e:
            self.logger.error(f"Get all payroll failed: {e}")
            return []

    def close_all(self):
        """Close all database connections"""
        for db_type, connection in self.connections.items():
            try:
                if db_type in ["sqlite", "postgresql"]:
                    connection.close()
                elif db_type == "mongodb":
                    connection.client.close()
                elif db_type == "redis":
                    connection.close()
                self.logger.info(f"Closed {db_type} connection")
            except Exception as e:
                self.logger.error(f"Error closing {db_type}: {e}")
