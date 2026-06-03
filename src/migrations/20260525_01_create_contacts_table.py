"""create contacts table

Revision ID: 20260525_01
"""

from yoyo import step


__depends__ = {}

steps = [
    step(
        """
        CREATE TABLE contacts (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(255) NOT NULL,
            message TEXT NOT NULL,
            created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
        );
        """,
        """
        DROP TABLE contacts;
        """,
    ),
    step(
        """
        CREATE INDEX ix_contacts_email ON contacts (email);
        """,
        """
        DROP INDEX ix_contacts_email;
        """,
    ),
]
