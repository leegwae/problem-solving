# HTML_파싱

https://www.acmicpc.net/problem/22859

## 문제

- 주어진 HTML 문자열을 파싱한다.
```HTML
<main>
    <div title="title_name_1">
        <p>paragraph 1</p>
        <p>paragraph 2 <i>Italic Tag</i> <br > </p>
        <p>paragraph 3 <b>Bold Tag</b> end.</p>
    </div>
    <div title="title_name_2">
        <p>paragraph 4</p>
        <p>paragraph 5 <i>Italic Tag 2</i> <br > end.</p>
    </div>
</main>
```

```
title : title_name_1
paragraph 1
paragraph 2 Italic Tag
paragraph 3 Bold Tag end.
title : title_name_2
paragraph 4
paragraph 5 Italic Tag 2 end.
```

## 아이디어

- 그냥 정직하게 풀었다. 처음과 끝이 확실하므로 `html.split('"title="')`로 `<div>`를 대략적으로 찾는다. 어차피 중요한 건 그 안의 `<p>~</p>`이기 때문이다.
- 대략적으로 구한 `<div>`를 `div.split('<p>')`로 대략적으로 `<p>`를 찾는다. 얻은 문자열들을 `</p>` 이후로 날리면 온전한 컨텐츠만 얻을 수 있다.
- 해당 컨텐츠를 시키는대로 파싱하면 끝

정규식 쓰면 간단하게 풀리는 거 같은데 정규식 잘 모르고 정규식 쓰지 말고 해보라는 말이 있어서 구현으로 풀어봤다.