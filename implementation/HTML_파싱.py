# # ======입력 양식=========
# # 항상 여는 태그 - 닫는 태그
# # <main></main>
# # ㄴ<div></div> 여러 개, <div title="제목">
# # ㄴㄴ<p></p> 여러 개
# # ㄴㄴㄴ<p> 사이에 다른 태그들이 공백을 두고 있다.
#
# # ====== <p> 파싱 =========
# # 1. <p> 안의 태그는 지운다
# # 2. 지우고 난 다음에 양쪽 공백 자른다.
# # 3. 공백 두 칸 이상은 한 칸으로 만든다.
# # 4. <p></p> 지운다.

import sys

input = sys.stdin.readline


def remove_tag(s: str) -> str:
	removed = ''

	tag = False
	for ch in s:
		if ch == '<':
			tag = True
			continue
		if ch == '>':
			tag = False
			continue
		if tag:
			continue

		removed += ch

	return removed


def remove_blank(s: str) -> str:
	removed = ''

	blank = False
	for ch in s:
		if ch == ' ':
			blank = True
			continue

		if blank:
			blank = False
			removed += ' '
		removed += ch

	return removed


def parse(s: str) -> str:
	tag_removed = remove_tag(s)
	stripped = tag_removed.strip()
	blank_removed = remove_blank(stripped)
	return blank_removed


if __name__ == '__main__':
	html = str(input())

	for div in html.split('title="')[1:]:
		title = div[:div.find('"')]
		print(f'title : {title}')
		for p in div.split('<p>')[1:]:
			parsed = parse(p[:p.rfind('</p>')])
			print(parsed)
