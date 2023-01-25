from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(
        TypeError
    ):  # se key e message não possuírem os tipos corretos
        encrypt_message(10, 10)
        encrypt_message(10, "ola")
        encrypt_message("ola", "10")

    assert (
        encrypt_message("ola", -1) == "alo"
    )  # se key não for um índice positivo válido de message
    assert encrypt_message("nezuko", 3) == "zen_oku"  # Se key for ímpar
    assert encrypt_message("nezuko", 4) == "ok_uzen"  # Se key for par
