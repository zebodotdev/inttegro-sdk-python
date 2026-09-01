"""Products resource for managing catalog products."""

from __future__ import annotations

from ..http_client import HttpClient


class Products:
    """Products resource for creating, updating, and managing products."""

    def __init__(self, http: HttpClient):
        self.http = http

    def create(self, payload: dict):
        """Create a product."""
        return self.http.post("/products/create", payload)

    def add_price(self, payload: dict):
        """Add a price to a product."""
        return self.http.post("/products/add_price", payload)

    def set_default_unit_price(self, payload: dict):
        """Set a product's default unit price."""
        return self.http.post("/products/set_default_unit_price", payload)

    def lookup(self, product_id: str):
        """Lookup a product by ID."""
        return self.http.post("/products/lookup", {"product_id": product_id})

    def update(self, payload: dict):
        """Update a product."""
        return self.http.post("/products/update", payload)

    def publish(self, product_id: str):
        """Publish a product."""
        return self.http.post("/products/publish", {"product_id": product_id})

    def unpublish(self, product_id: str):
        """Unpublish a product."""
        return self.http.post("/products/unpublish", {"product_id": product_id})

    def archive(self, product_id: str):
        """Archive a product."""
        return self.http.post("/products/archive", {"product_id": product_id})

    def page(self, payload: dict | None = None):
        """Page through products."""
        return self.http.post("/products/page", payload or {})
