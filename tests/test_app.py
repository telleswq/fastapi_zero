from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ola_mundo():
    """ "
    Esse teste tem 3 etapas (AAA):
    - Arrange: (arranjo)preparar o ambiente para o teste
    - Act: (ação) executar a ação que queremos testar
    - Assert: (afirmação) verificar se o resultado é o esperado
    """
    # Arrange
    client = TestClient(app)
    # Act
    response = client.get('/')
    # Assert
    assert response.json() == {'message': 'Hello World'}
    assert response.status_code == HTTPStatus.OK
