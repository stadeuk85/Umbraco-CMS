import unittest
from runtime.visibility_pipeline import validate_jsonld, measure_visibility, normalize_url
from runtime.umbraco_delivery_reader import UmbracoDeliveryReader

class PipelineTests(unittest.TestCase):
    def test_invalid_json(self):
        self.assertFalse(validate_jsonld("{")["valid"])
    def test_duplicate_ids(self):
        doc = '{"@graph":[{"@type":"Person","@id":"x"},{"@type":"Organization","@id":"x"}]}'
        self.assertFalse(validate_jsonld(doc)["valid"])
    def test_visible_fact_mismatch(self):
        self.assertFalse(validate_jsonld('{"@type":"Article","headline":"A"}', {"headline":"B"})["valid"])
    def test_valid(self):
        self.assertTrue(validate_jsonld('{"@type":"Article","headline":"A"}', {"headline":"A"})["valid"])
    def test_grouped_metrics_and_not_tested(self):
        rows = [
            {"platform":"ChatGPT Search","search_mode":"web","market":"UK","locale":"en-GB","status":"OBSERVED","brand_mentioned":True,"citations":["https://www.example.org/article?tracking=1"]},
            {"platform":"ChatGPT Search","search_mode":"web","market":"UK","locale":"en-GB","status":"NOT_TESTED"},
            {"platform":"Claude","search_mode":"offline","market":"UK","locale":"en-GB","status":"OBSERVED","citations":[]}
        ]
        result = measure_visibility(rows, {"example.org"})["groups"]
        chat = next(r for r in result if r["platform"] == "ChatGPT Search")
        self.assertEqual(chat["not_tested"], 1)
        self.assertEqual(chat["citation_coverage"], 1)
        self.assertEqual(chat["eligible"], 1)
    def test_url_normalisation(self):
        self.assertEqual(normalize_url("https://EXAMPLE.org/x/?q=a"), "https://example.org/x")
    def test_reader_refuses_wrong_host(self):
        with self.assertRaises(ValueError):
            UmbracoDeliveryReader("https://evil.example", "approved.example")
    def test_reader_refuses_write(self):
        r = UmbracoDeliveryReader("https://approved.example", "approved.example")
        with self.assertRaises(PermissionError):
            r.draft_write()

if __name__ == "__main__":
    unittest.main()
