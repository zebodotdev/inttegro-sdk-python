## [Unreleased]

## [3.0.0] - 2026-09-03

- Breaking: every documented resource method now returns an immutable domain dataclass or page directly.
- Internalized the dynamic fallback value and removed the public response wrapper module.
- Renamed `PaymentResponseStatus` to `PaymentResultStatus`.

## [2.1.0] - 2026-09-03

- Replaced dictionary-shaped request contracts with immutable, keyword-only request dataclasses.
- Added resource request namespaces such as `inttegro.orders.CreateRequest` and recursively serialize nested request objects.
- Preserved dictionary payload support for backwards compatibility.

## [2.0.0] - 2026-09-02

- Made the generated model module private; public types are imported directly from `inttegro`.
- Added OpenAPI-generated immutable dataclass response models and typed nested fields.
- Added generated `TypedDict` request contracts and endpoint-specific resource return types.
- Added PEP 561 package metadata plus strict mypy and Pyright checks in CI.
- Preserved attribute access, mapping access, `to_dict()`, and unknown response fields.

## [1.0.0] - 2026-09-01

- Breaking: renamed the distribution, import package, client, and base exception to `inttegro`, `InttegroClient`, and `InttegroError`.
- Aligned package metadata, examples, and the transport user agent with the public Inttegro service name.
