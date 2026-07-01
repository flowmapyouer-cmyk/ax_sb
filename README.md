# 세컨부스트 — 독자별 산출물 대시보드

비정형 요구사항(슬랙 DM·카카오톡·CS 이메일·구두 회의록)을 15케이스 표준 PRD로 구조화하고,
읽는 사람(실무자/고객사/경영진)에 따라 형식·언어·강조점이 다른 산출물 3종을 자동 생성하는
파이프라인의 결과물입니다.

## 보는 법

- **`index.html`** — 이 저장소의 메인 페이지. 독자별 탭(세컨부스트 실무자 / 고객사 / 세컨부스트 경영진)을
  눌러 요약·배경·우선순위 판단 로직·산출물 미리보기를 확인할 수 있습니다. 각 탭 하단에서 전체 문서를
  복사하거나 다운로드할 수 있습니다.
  - GitHub Pages로 열람: 저장소 Settings → Pages → Branch를 `main`으로 설정하면
    `https://<사용자명>.github.io/ax_sb/` 에서 바로 볼 수 있습니다.
  - 로컬에서 열람: `index.html`을 더블클릭해 브라우저로 바로 열어도 동일하게 동작합니다.
  - **share.streamlit.io로 배포**: `streamlit_app.py`가 `index.html`을 그대로 임베드하는
    Streamlit 앱입니다. Main file path를 `streamlit_app.py`로 지정하면 배포됩니다
    (`requirements.txt`에 `streamlit` 의존성 포함).

## 폴더 구조

```
index.html              대시보드 메인 페이지 (독자별 탭 UI)
outputs/                실제 제출 산출물 3종 (PDF 원본)
  ├─ 스프린트_실행.pdf                    PM-prompt.md 실행 결과 — 내부 개발/관리용 PRD
  ├─ 세컨부스트_고객사_합의용_기획서.pdf    customer-prompt.md 실행 결과 — 고객사 합의용 기획서
  └─ 스펙_리스크_의사결정_요청서.pdf        challenge-prompt-v3.md 실행 결과 — 경영진용 의사결정 요청서
source/                 위 3개 산출물을 만들어내는 스킬(프롬프트)과 설계 근거 문서
  ├─ problem.md                    과제 배경·미션 정의
  ├─ CLAUDE.md                     레벨(Basic/Standard/Challenge)별 채점 기준 및 작업 지침
  ├─ context/
  │   ├─ company-info.md           세컨부스트 도메인 컨텍스트, PRD 표준, 우선순위 판단 기준
  │   └─ industry-news.md          비정형 텍스트 처리·PRD 자동화 관련 업계 동향
  └─ output/
      ├─ priority-matrix.md        P1/P2/P3 판정 매트릭스 (6대 축 복합 판단) — 설계 근거
      ├─ challenge-matrix.md       Blocker/Warning/참조 판정 매트릭스 — 설계 근거
      ├─ PM-prompt.md              실무자용 PRD 생성 스킬 프롬프트 → outputs/스프린트_실행.pdf
      ├─ customer-prompt.md        고객사용 기획서 생성 스킬 프롬프트 → outputs/세컨부스트_고객사_합의용_기획서.pdf
      ├─ challenge-prompt-v3.md    경영진용 의사결정 요청서 생성 스킬 프롬프트 → outputs/스펙_리스크_의사결정_요청서.pdf
      └─ template.md               PRD 5섹션 출력 템플릿
```

## 매핑 요약

| 스킬(프롬프트) | 독자 | 산출물 |
|---|---|---|
| `source/output/PM-prompt.md` | 세컨부스트 실무자 | `outputs/스프린트_실행.pdf` |
| `source/output/customer-prompt.md` | 고객사(창업자·기획자) | `outputs/세컨부스트_고객사_합의용_기획서.pdf` |
| `source/output/challenge-prompt-v3.md` | 세컨부스트 경영진(C-Level) | `outputs/스펙_리스크_의사결정_요청서.pdf` |
