def get_prompt(zastosowanie):
    prompts = {
        'opis_produktu': 'Jako profesjonalny copywriter, stwórz atrakcyjny opis dla {nazwa produktu} z {cechy produktu}.',
        'artykul': 'Jako profesjonalny copywriter, napisz angażujący artykuł na bloga na temat {temat}.',
        'recenzja': 'Jako ekspert w {branża}, napisz profesjonalną recenzję dla {produkt/usługa}.',
        'pomysly_na_artykul': 'Jesteś kreatywnym generatorem pomysłów na artykuły blogowe. Wymyśl różnorodne propozycje na temat {temat}.',
        'nazwa_dla_firmy': 'Jesteś ekspertem w tworzeniu nazw dla firm i projektów. Stwórz unikalną i kreatywną nazwę dla {opis firmy/projektu}.',
        'pomysly_na_firme': 'Jako specjalista w generowaniu pomysłów na startupy, podaj innowacyjne propozycje związane z branżą, która przekaże ci użytkownik.',
        'wezwanie_do_dzialania': 'Jako doświadczony copywriter, stwórz przekonujące wezwanie do działania dla {produkt/usługa}.',
        'list_motywacyjny': 'Jesteś ekspertem w pisaniu listów motywacyjnych. Napisz list motywacyjny dla {stanowisko} w {nazwa firmy}.',
        'email': 'Jako profesjonalny redaktor, sformułuj {typ emaila} dotyczący {temat}.',
        'reklama': 'Jako specjalista ds. reklamy w mediach społecznościowych, stwórz krótki tekst reklamowy promujący {produkt/usługa} na {platforma}.',
        'pytania_do_wywiadu': 'Jesteś ekspertem w tworzeniu pytań do wywiadów. Wymyśl interesujące pytania na wywiad z {imię i nazwisko} na temat {temat}.',
        'opis_oferty_pracy': 'Jako doświadczony copywriter, napisz opis stanowiska dla {stanowisko} w {nazwa firmy}.',
        'generator_slow_kluczowych': 'Jako specjalista SEO, podaj listę słów kluczowych związanych z {temat}.',
        'pomysly_na_posty': 'Jesteś kreatywnym generatorem pomysłów na posty w mediach społecznościowych. Zaproponuj angażujące posty dla {nazwa firmy/profil} na {platforma}.',
        'opis_profilu': 'Jesteś ekspertem w pisaniu opisów profilu. Napisz krótki i kreatywny opis profilu dla {imię i nazwisko} na {platforma}.',
        'pytania_i_odpowiedzi': 'Jako specjalista w dziedzinie {temat}, odpowiedz na 5 najczęściej zadawanych pytań dotyczących {temat}.',
        'odpowiedz_na_recenzje': 'Jako profesjonalny specjalista ds. obsługi klienta, napisz odpowiedź na {typ recenzji/wiadomości} dotyczącą {produkt/usługa}.',
        'seo_meta_tytul': 'Jako ekspert SEO, stwórz optymalny meta tytuł dla strony internetowej na temat {temat}.',
        'seo_meta_opis': 'Jako ekspert SEO, napisz efektywny meta opis dla strony internetowej na temat {temat}.',
        'tekst_piosenki': 'Jesteś utalentowanym tekściarzem. Napisz tekst piosenki na temat {temat} w stylu {gatunek muzyczny}.',
        'zaswiadczenie': 'Jako ekspert w {branża}, napisz profesjonalną recenzję dla {produkt/usługa}.',
        'yt_opis_kanalu': 'Jako specjalista ds. treści wideo, stwórz angażujący opis kanału YouTube dla {nazwa kanału} na temat {temat}.',
        'yt_opis_filmu': 'Jako specjalista ds. treści wideo, napisz interesujący opis filmu YouTube dla {nazwa filmu} na temat {temat}.',
        'yt_pomysly_na_film': 'Jesteś kreatywnym generatorem pomysłów na filmy YouTube. Wymyśl różnorodne propozycje na temat {temat} dla {nazwa kanału}.'
    }

    if zastosowanie in prompts:
        return prompts[zastosowanie]
    else:
        return "Nieznane zastosowanie."


# Przykład użycia
zastosowanie = 'pomysly_na_artykul'
prompt = get_prompt(zastosowanie)
print(prompt)
