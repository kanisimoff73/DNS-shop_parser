import requests

cookies = {
    'lang': 'ru',
    'phonesIdent': 'e63db7b89c328b863f6e3b63642bb1b2d6b7b6bc53ad12f8a24487f774d6aeeca%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%2269401c39-7c42-451f-bb3c-19f1db8a5620%22%3B%7D',
    '_ym_uid': '1692347992731602538',
    '_ym_d': '1692347992',
    'city_path': 'barnaul',
    'current_path': 'bac6da453e264a9b8261385cee3496abc6f588491f0871d236621899ac9a4727a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A121%3A%22%7B%22city%22%3A%2249bc7ffa-ddec-11dc-8709-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu0411%5Cu0430%5Cu0440%5Cu043d%5Cu0430%5Cu0443%5Cu043b%22%2C%22method%22%3A%22manual%22%7D%22%3B%7D',
    'date-user-last-order-v2': 'ac51acaa955bd0daa41fa459a9d7ac9a958d13472e907db85492dc29dd206450a%3A2%3A%7Bi%3A0%3Bs%3A23%3A%22date-user-last-order-v2%22%3Bi%3A1%3Bi%3A1693176546%3B%7D',
    'rrpvid': '283398266082883',
    'rcuid': '64df2e4fa13cf043a78ca8fa',
    '_gcl_au': '1.1.1736129422.1694653055',
    '_ab_1_': '333',
    'tmr_lvid': '2490cba45e6cc404e27b6e2b91c4888e',
    'tmr_lvidTS': '1694653055075',
    'PHPSESSID': '83374ac724122b47b8d6dbbdddc510c2',
    '_csrf': '405b5eeb809a829e8c6f84abec5e764dd0887c429fa87779003a59ff0dec791ea%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22m-C_12PWI0VnaGHCqadMhnfknH3wmfze%22%3B%7D',
    '_ab_': '%7B%22search-sandbox%22%3A%22default%22%2C%22catalog-hit-filter%22%3A%22filtr_hit_test%22%2C%22header-link%22%3A%22head_career%22%7D',
    'auth_public_uid': '7586c7457c7c69db16282de679d4828d',
    'cartUserCookieIdent_v3': '2a6731b80887616297636482ae137a946dc15473479ae85d027182f60153ec83a%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%226dae66c4-a7b8-39e5-b786-8752bcbb0261%22%3B%7D',
    '_gid': 'GA1.2.1340699602.1695995361',
    'expert-sender-subscribed-user': 'eb3fc420fba5a75ca50c5cefd724a76603ac6c398a03962429f639935c6d3526a%3A2%3A%7Bi%3A0%3Bs%3A29%3A%22expert-sender-subscribed-user%22%3Bi%3A1%3Bb%3A1%3B%7D',
    'cf_avails': 'now',
    '_ym_isad': '1',
    'qrator_jsr': '1696241655.240.gi7dAHBYf9MIfnoe-ohdf8ud030nf6lbk06udpr3t2mbt9hod-00',
    'qrator_jsid': '1696241655.240.gi7dAHBYf9MIfnoe-1qv86u7ulhao2977c71j3n5uvbamtjn9',
    'auth_access_token': 'eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoU1NJRCI6IjY4NmQ4YjM5MjlhN2M5YzI3MjQzMDI1MmZkMzNlNzk2N2VjN2JiYzQ1MzZiNmVlNjk4NTc5ZWFhZmI0MTFmYjIiLCJleHAiOjE2OTYyNDI1NTUsInJuZCI6IjAyZmMxMjIxNWRlMGMzYzIwYzY3ODYyOWY5ZGJkMzc1Zjk3NWQyZWFmYjEwMDYzMTZmZmQ5YjgzNzJiYTlkMWUiLCJ1c2VySWQiOiIzOGY2YmZiNy03MmM2LTljMjYtNTA4Ny1iODM1MDAzNjQ5ZDkiLCJ1c2VyTmFtZSI6IiJ9.MEUCIQCwNYoWQo0BLaWpoxGtQ4iTioPVyIDeh4_lRD6fXee8gQIgQActfXwBU0kpKCBhkicZfaqJbpcqZaRjJOpf_k_LneA',
    'auth_refresh_token': '546cc3d5371ff47b261130962b4391c4cf02b609a4f399e6a25b042a08819b34',
    'auth_ssid': '686d8b3929a7c9c272430252fd33e7967ec7bbc4536b6ee698579eaafb411fb2',
    '_gat': '1',
    '_gat_%5Bobject%20Object%5D': '1',
    '_gat_UA-8349380-2': '1',
    '_ga_FLS4JETDHW': 'GS1.1.1696241657.18.0.1696241658.59.0.0',
    '_ym_visorc': 'b',
    'tmr_detect': '0%7C1696241660551',
    '_ga': 'GA1.2.936029667.1694653054',
    '_ga_YT23VHSRDB': 'GS1.2.1696241657.16.0.1696241672.45.0.0',
}

headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'lang=ru; phonesIdent=e63db7b89c328b863f6e3b63642bb1b2d6b7b6bc53ad12f8a24487f774d6aeeca%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%2269401c39-7c42-451f-bb3c-19f1db8a5620%22%3B%7D; _ym_uid=1692347992731602538; _ym_d=1692347992; city_path=barnaul; current_path=bac6da453e264a9b8261385cee3496abc6f588491f0871d236621899ac9a4727a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A121%3A%22%7B%22city%22%3A%2249bc7ffa-ddec-11dc-8709-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu0411%5Cu0430%5Cu0440%5Cu043d%5Cu0430%5Cu0443%5Cu043b%22%2C%22method%22%3A%22manual%22%7D%22%3B%7D; date-user-last-order-v2=ac51acaa955bd0daa41fa459a9d7ac9a958d13472e907db85492dc29dd206450a%3A2%3A%7Bi%3A0%3Bs%3A23%3A%22date-user-last-order-v2%22%3Bi%3A1%3Bi%3A1693176546%3B%7D; rrpvid=283398266082883; rcuid=64df2e4fa13cf043a78ca8fa; _gcl_au=1.1.1736129422.1694653055; _ab_1_=333; tmr_lvid=2490cba45e6cc404e27b6e2b91c4888e; tmr_lvidTS=1694653055075; PHPSESSID=83374ac724122b47b8d6dbbdddc510c2; _csrf=405b5eeb809a829e8c6f84abec5e764dd0887c429fa87779003a59ff0dec791ea%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22m-C_12PWI0VnaGHCqadMhnfknH3wmfze%22%3B%7D; _ab_=%7B%22search-sandbox%22%3A%22default%22%2C%22catalog-hit-filter%22%3A%22filtr_hit_test%22%2C%22header-link%22%3A%22head_career%22%7D; auth_public_uid=7586c7457c7c69db16282de679d4828d; cartUserCookieIdent_v3=2a6731b80887616297636482ae137a946dc15473479ae85d027182f60153ec83a%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%226dae66c4-a7b8-39e5-b786-8752bcbb0261%22%3B%7D; _gid=GA1.2.1340699602.1695995361; expert-sender-subscribed-user=eb3fc420fba5a75ca50c5cefd724a76603ac6c398a03962429f639935c6d3526a%3A2%3A%7Bi%3A0%3Bs%3A29%3A%22expert-sender-subscribed-user%22%3Bi%3A1%3Bb%3A1%3B%7D; cf_avails=now; _ym_isad=1; qrator_jsr=1696241655.240.gi7dAHBYf9MIfnoe-ohdf8ud030nf6lbk06udpr3t2mbt9hod-00; qrator_jsid=1696241655.240.gi7dAHBYf9MIfnoe-1qv86u7ulhao2977c71j3n5uvbamtjn9; auth_access_token=eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoU1NJRCI6IjY4NmQ4YjM5MjlhN2M5YzI3MjQzMDI1MmZkMzNlNzk2N2VjN2JiYzQ1MzZiNmVlNjk4NTc5ZWFhZmI0MTFmYjIiLCJleHAiOjE2OTYyNDI1NTUsInJuZCI6IjAyZmMxMjIxNWRlMGMzYzIwYzY3ODYyOWY5ZGJkMzc1Zjk3NWQyZWFmYjEwMDYzMTZmZmQ5YjgzNzJiYTlkMWUiLCJ1c2VySWQiOiIzOGY2YmZiNy03MmM2LTljMjYtNTA4Ny1iODM1MDAzNjQ5ZDkiLCJ1c2VyTmFtZSI6IiJ9.MEUCIQCwNYoWQo0BLaWpoxGtQ4iTioPVyIDeh4_lRD6fXee8gQIgQActfXwBU0kpKCBhkicZfaqJbpcqZaRjJOpf_k_LneA; auth_refresh_token=546cc3d5371ff47b261130962b4391c4cf02b609a4f399e6a25b042a08819b34; auth_ssid=686d8b3929a7c9c272430252fd33e7967ec7bbc4536b6ee698579eaafb411fb2; _gat=1; _gat_%5Bobject%20Object%5D=1; _gat_UA-8349380-2=1; _ga_FLS4JETDHW=GS1.1.1696241657.18.0.1696241658.59.0.0; _ym_visorc=b; tmr_detect=0%7C1696241660551; _ga=GA1.2.936029667.1694653054; _ga_YT23VHSRDB=GS1.2.1696241657.16.0.1696241672.45.0.0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'virtual_category_uid': 'd17f27fbd8b001f0',
    'utm_source': 'www.dns-shop.ru',
}

response = requests.get(
    'https://www.dns-shop.ru/catalog/17a9d40a16404e77/nastolnye-chasy/',
    params=params,
    cookies=cookies,
    headers=headers,
)

headers_retail_rocket_product = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'lang=ru; phonesIdent=e63db7b89c328b863f6e3b63642bb1b2d6b7b6bc53ad12f8a24487f774d6aeeca%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%2269401c39-7c42-451f-bb3c-19f1db8a5620%22%3B%7D; _ym_uid=1692347992731602538; _ym_d=1692347992; city_path=barnaul; current_path=bac6da453e264a9b8261385cee3496abc6f588491f0871d236621899ac9a4727a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A121%3A%22%7B%22city%22%3A%2249bc7ffa-ddec-11dc-8709-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu0411%5Cu0430%5Cu0440%5Cu043d%5Cu0430%5Cu0443%5Cu043b%22%2C%22method%22%3A%22manual%22%7D%22%3B%7D; date-user-last-order-v2=ac51acaa955bd0daa41fa459a9d7ac9a958d13472e907db85492dc29dd206450a%3A2%3A%7Bi%3A0%3Bs%3A23%3A%22date-user-last-order-v2%22%3Bi%3A1%3Bi%3A1693176546%3B%7D; rrpvid=283398266082883; rcuid=64df2e4fa13cf043a78ca8fa; _gcl_au=1.1.1736129422.1694653055; _ab_1_=333; tmr_lvid=2490cba45e6cc404e27b6e2b91c4888e; tmr_lvidTS=1694653055075; PHPSESSID=83374ac724122b47b8d6dbbdddc510c2; _csrf=405b5eeb809a829e8c6f84abec5e764dd0887c429fa87779003a59ff0dec791ea%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22m-C_12PWI0VnaGHCqadMhnfknH3wmfze%22%3B%7D; _ab_=%7B%22search-sandbox%22%3A%22default%22%2C%22catalog-hit-filter%22%3A%22filtr_hit_test%22%2C%22header-link%22%3A%22head_career%22%7D; auth_public_uid=7586c7457c7c69db16282de679d4828d; cartUserCookieIdent_v3=2a6731b80887616297636482ae137a946dc15473479ae85d027182f60153ec83a%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%226dae66c4-a7b8-39e5-b786-8752bcbb0261%22%3B%7D; _gid=GA1.2.1340699602.1695995361; expert-sender-subscribed-user=eb3fc420fba5a75ca50c5cefd724a76603ac6c398a03962429f639935c6d3526a%3A2%3A%7Bi%3A0%3Bs%3A29%3A%22expert-sender-subscribed-user%22%3Bi%3A1%3Bb%3A1%3B%7D; cf_avails=now; qrator_jsr=1696298769.069.9THaTnbRx6c3IANf-tkm57171ecebcos9o9ns66rmv5hk4mlr-00; qrator_ssid=1696298770.197.qKZj1i6JH4LsxPMX-cl0aucj31hcs2j1tfh9cbe8mpebep0h9; qrator_jsid=1696298769.069.9THaTnbRx6c3IANf-t81cr1puk4kusu53bl5sn4f51ba5bngc; auth_access_token=eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoU1NJRCI6IjQ1NjBmYTFiNGE5ZmNjNjgxNjllMDc0YWM1MjA2ZTY2NDk0ZDIwMTBjMDI4MzZlNDFkYjgyMDU2YWIxZmY1NjUiLCJleHAiOjE2OTYyOTk2NzMsInJuZCI6IjE4NjRkYzQwNTI4ODhlZjE2NGVmMzVmYjQwZTM0NzYzMDk2MzI3MGVhMGE5YjFkODYzZmU5YTgzYjc5ZWE4N2IiLCJ1c2VySWQiOiIzOGY2YmZiNy03MmM2LTljMjYtNTA4Ny1iODM1MDAzNjQ5ZDkiLCJ1c2VyTmFtZSI6IiJ9.MEUCIQCGsiDEDF6p21L1OJFYsmoAcXkxlV-wfZ_OzU_nqWtqmQIgIYhDP5wEoz2Z5A0-f9QhBLHN9nwg6_zEBE79l1yvhPI; auth_refresh_token=e8d203b0054adf2fff5e570ec1e57d29ee9e8fa391bcf9360c2f9f3a9b9b3c47; auth_ssid=4560fa1b4a9fcc68169e074ac5206e66494d2010c02836e41db82056ab1ff565; _ym_isad=1; _ym_visorc=b; tmr_detect=0%7C1696298784838; _gat_UA-8349380-2=1; _ga_YT23VHSRDB=GS1.2.1696298776.17.0.1696298876.60.0.0; rr-testCookie=testvalue; _gat=1; _ga=GA1.2.936029667.1694653054; _gat_%5Bobject%20Object%5D=1; _ga_FLS4JETDHW=GS1.1.1696298775.19.1.1696298886.49.0.0',
    'Origin': 'https://www.dns-shop.ru',
    'Referer': 'https://www.dns-shop.ru/product/5465b6c801bd1b80/casy-dexp-rc-240/no-referrer',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'X-CSRF-Token': 'PSeRZ9z_kvumwW1Zu_T5BELn1XwMTpXPzv0vUC1hUyRQCtI47c3CrO_xOzfas7FHM4axMWQg86SgtRwnQAcpQQ==',
    'X-Requested-With': 'XMLHttpRequest',
    'content-type': 'application/x-www-form-urlencoded',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
