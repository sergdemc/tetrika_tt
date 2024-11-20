from unittest.mock import Mock, patch
from task2.solution import fetch_page, get_animals_count, save_to_csv, main
import requests


def test_fetch_page():
    with patch("requests.Session.get") as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = "<html></html>"
        mock_get.return_value = mock_response

        with requests.Session() as session:
            url = "https://example.com"
            response = fetch_page(session, url)

            assert response == "<html></html>"

            mock_get.assert_called_once_with(url)


@patch("task2.solution.fetch_page")
def test_get_animals_count(mock_fetch_page):
    mock_html = """
    <div class="mw-category-group">
        <h3>А</h3>
        <ul>
            <li>Аист</li>
            <li>Акула</li>
        </ul>
    </div>
    <a href="/wiki/Категория:Животные_по_алфавиту?page=2">Следующая страница</a>
    """
    mock_fetch_page.side_effect = [mock_html, ""]

    counts = get_animals_count()
    assert counts == {"А": 2}


def test_save_to_csv(tmp_path):
    counts = {"А": 3, "Б": 2}
    file_path = tmp_path / "test.csv"
    save_to_csv(counts, filename=file_path)

    with open(file_path, encoding="utf-8") as file:
        lines = file.readlines()
    assert lines == ["А,3\n", "Б,2\n"]


@patch("task2.solution.get_animals_count")
@patch("task2.solution.save_to_csv")
def test_main(mock_save_to_csv, mock_get_animals_count):
    mock_get_animals_count.return_value = {"А": 3}
    main()
    mock_get_animals_count.assert_called_once()
    mock_save_to_csv.assert_called_once_with({"А": 3})
