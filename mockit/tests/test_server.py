import requests

import xml.etree.ElementTree as ET

from mock_server import MockitServer


class TestPersonalities:
    @classmethod
    def setup_class(cls):
        cls.m_s = MockitServer()

        # Mock Json Endpoints.
        cls.m_s.add_json_response(
            url="/json_endpoint", serializable={"endpoint": "json"}, methods=("GET",)
        )

        # Mock XML Endpoints.
        cls.m_s.add_string_response(
            url="/xml_endpoint",
            response="""
            <xml-tag>
                <tag>text</tag>
            </xml-tag>
        """,
            methods=("GET",),
        )

        # Start mock service.
        cls.m_s.start()

    def test_json_endpoint(self):
        """
        Test JSON endpoint functionality.
        """

        response = requests.get(f"{self.m_s.url}/json_endpoint")

        assert response.status_code == 200
        assert "endpoint" in response.json()

    def test_xml_response(self):
        """
        Test XML response functionality.
        """
        response = requests.get(f"{self.m_s.url}/xml_endpoint")
        response_xml = ET.fromstring(response.text)
        assert response.status_code == 200
        assert response_xml.tag == "xml-tag"

    @classmethod
    def teardown_class(cls):
        cls.m_s.terminate()
