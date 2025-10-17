CREATE TABLE password_manager (
    id SERIAL PRIMARY KEY,
    service_name TEXT NOT NULL,
    login TEXT NOT NULL,
    password TEXT NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE UNIQUE INDEX uniq_service_login
ON password_manager (service_name, login);

SELECT * FROM password_manager;


