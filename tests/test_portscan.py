from unittest.mock import MagicMock, patch
from connect import tryConnection

# Teste com mock (Garante a lógica sem depender de internet)
@patch('socket.socket')
def test_tryConnection_porta_aberta_mock(mock_socket):
    mock_instance = MagicMock()
    mock_instance.connect_ex.return_value = 0  # Simula porta aberta
    mock_socket.return_value = mock_instance

    tryConnection(80, "127.0.0.1")
    mock_instance.connect_ex.assert_called_once_with(("127.0.0.1", 80))
    mock_instance.close.assert_called_once()


def test_tryConnection_porta_fechada():
    # Porta alta que normalmente está fechada
    porta_fechada = 49151 
    tryConnection(porta_fechada, "127.0.0.1")
