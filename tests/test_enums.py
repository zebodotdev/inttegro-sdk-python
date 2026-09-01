import json
import unittest

from inttegro import ProductType, RefundReason, UploadRequestStatus


class ApiEnumTest(unittest.TestCase):
    def test_wire_enums_are_public_and_json_compatible(self):
        encoded = json.dumps(
            {
                "product": ProductType.DIGITAL,
                "refund": RefundReason.REQUESTED_BY_CUSTOMER,
                "status": UploadRequestStatus.PENDING,
            }
        )
        self.assertEqual(
            encoded,
            '{"product": "digital", "refund": "requested_by_customer", "status": "pending"}',
        )


if __name__ == "__main__":
    unittest.main()
