<h1>Mockit - Easy REST API Mock</h1>

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A very simple to use mock server which runs in a separate process,
 can be easily used with pytest.

It allows to mock JSON and String responses using all available HTTP methods(GET, POST, PUT, PATCH, DELETE, ext..).



<h3>Installation:</h3>

Install with pip:
```buildoutcfg
$ pip install mockit
```


<h3>Examples:</h3>
<h5> Get Started: </h5>
```python
from mockit import MockitServer


m_s = MockitServer()

# Mock Json Endpoints.
m_s.add_json_response(url="/json_endpoint", serializable={"endpoint": "json"}, methods=("GET", ))

# Mock XML Endpoints.
m_s.add_string_response(
    url="/xml_endpoint",
    response="""
    <xml-tag>
        <tag>text</tag>
    </xml-tag>
""", methods=("GET", )
)

# Start mock service.
m_s.start()
```


<h5> With Pytest: </h5> 

```python
import requests

from mock_service import MockServer


class TestPersonalities:
    @classmethod
    def setup_class(cls):
        cls.m_s = MockServer()

        # Mock Json Endpoints.
        cls.m_s.add_json_response(url="/json_endpoint", serializable={"endpoint": "json"}, methods=("GET", ))

        # Start mock service.
        cls.m_s.start()


    def test_json_endpoint(self):

        response = requests.get(f"{self.m_s.url}/json_endpoint")

        assert response.status_code == 200
        assert "endpoint" in response.json()

    @classmethod
    def teardown_class(cls):
        cls.m_s.terminate()
```

<h3>Features:</h3>
<li>Mocking REST API.</li>
<li>Mocking JSON, XML and String responses.</li>


<h3>Bug report:</h3>

If you have any trouble, report bug at GitHub Issue https://github.com/victorvasiliev/mockit/issues
