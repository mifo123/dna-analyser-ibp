from types import SimpleNamespace

import DNA_analyser_IBP.adapters.cpg_adapter as cpg_adapter_module
import DNA_analyser_IBP.adapters.g4hunter_adapter as g4hunter_adapter_module
import DNA_analyser_IBP.adapters.rloopr_adapter as rloopr_adapter_module
import DNA_analyser_IBP.adapters.zdna_adapter as zdna_adapter_module
from DNA_analyser_IBP.adapters.cpg_adapter import CpGAdapter
from DNA_analyser_IBP.adapters.g4hunter_adapter import G4HunterAdapter
from DNA_analyser_IBP.adapters.rloopr_adapter import RLooprAdapter
from DNA_analyser_IBP.adapters.zdna_adapter import ZDnaAdapter
from DNA_analyser_IBP.models import User


def _user() -> User:
    user = User(email="test@test.cz", password="password", server="http://localhost")
    user.jwt = "jwt"
    return user


def test_g4hunter_export_bedgraph(monkeypatch):
    captured = {}

    def fake_get(url, headers, params):
        captured["url"] = url
        captured["headers"] = headers
        captured["params"] = params
        return SimpleNamespace(status_code=200, text="content")

    monkeypatch.setattr(g4hunter_adapter_module.requests, "get", fake_get)
    monkeypatch.setattr(
        g4hunter_adapter_module,
        "validate_text_response",
        lambda response, status_code: response.text,
    )

    adapter = G4HunterAdapter(user=_user())
    content = adapter.export_bedgraph(id="analyse-id", aggregate=False)

    assert content == "content"
    assert captured["url"].endswith("/analyse/g4hunter/analyse-id/quadruplex.bedgraph")
    assert captured["params"] == {"aggregate": "false"}


def test_cpg_export_bedgraph(monkeypatch):
    captured = {}

    def fake_get(url, headers):
        captured["url"] = url
        captured["headers"] = headers
        return SimpleNamespace(status_code=200, text="content")

    monkeypatch.setattr(cpg_adapter_module.requests, "get", fake_get)
    monkeypatch.setattr(
        cpg_adapter_module,
        "validate_text_response",
        lambda response, status_code: response.text,
    )

    adapter = CpGAdapter(user=_user())
    content = adapter.export_bedgraph(id="analyse-id")

    assert content == "content"
    assert captured["url"].endswith("/analyse/cpg/analyse-id/cpg.bedgraph")


def test_rloopr_export_bedgraph(monkeypatch):
    captured = {}

    def fake_get(url, headers):
        captured["url"] = url
        captured["headers"] = headers
        return SimpleNamespace(status_code=200, text="content")

    monkeypatch.setattr(rloopr_adapter_module.requests, "get", fake_get)
    monkeypatch.setattr(
        rloopr_adapter_module,
        "validate_text_response",
        lambda response, status_code: response.text,
    )

    adapter = RLooprAdapter(user=_user())
    content = adapter.export_bedgraph(id="analyse-id")

    assert content == "content"
    assert captured["url"].endswith("/analyse/rloopr/analyse-id/rloopr.bedgraph")


def test_zdna_export_bedgraph(monkeypatch):
    captured = {}

    def fake_get(url, headers):
        captured["url"] = url
        captured["headers"] = headers
        return SimpleNamespace(status_code=200, text="content")

    monkeypatch.setattr(zdna_adapter_module.requests, "get", fake_get)
    monkeypatch.setattr(
        zdna_adapter_module,
        "validate_text_response",
        lambda response, status_code: response.text,
    )

    adapter = ZDnaAdapter(user=_user())
    content = adapter.export_bedgraph(id="analyse-id")

    assert content == "content"
    assert captured["url"].endswith("/analyse/zdna/analyse-id/zdna.bedgraph")
