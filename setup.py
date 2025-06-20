from setuptools import setup, find_packages

setup(
    name="python_api_template",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "fastapi>=0.95.0,<0.96.0",
        "uvicorn>=0.22.0,<0.23.0",
        "pydantic>=1.10.7,<2.0.0",
        "python-dotenv>=1.0.0,<2.0.0",
        "sqlalchemy>=2.0.12,<2.1.0",
        "asyncpg>=0.27.0,<0.28.0",
        "alembic>=1.10.4,<1.11.0",
        "psycopg2-binary>=2.9.6,<3.0.0",
        "httpx>=0.24.0,<0.25.0",
        "python-multipart>=0.0.6,<0.1.0",
        "python-jose>=3.3.0,<3.4.0",
        "passlib>=1.7.4,<1.8.0",
    ],
    python_requires=">=3.10",
    description="A template for building Python APIs with FastAPI and PostgreSQL",
    author="Eric Khein",
    author_email="your.email@example.com",
    url="https://github.com/erickhv92/python-api-template",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
)