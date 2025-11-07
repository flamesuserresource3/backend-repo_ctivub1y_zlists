"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: EmailStr = Field(..., description="Email address")
    password_hash: str = Field(..., description="Hashed password (server-side only)")
    role: Literal["student", "hod", "tpo"] = Field(..., description="User role")
    department: Optional[str] = Field(None, description="Department name if applicable")
    is_active: bool = Field(True, description="Whether user is active")
