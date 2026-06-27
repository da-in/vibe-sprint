# vibe sprint

해커톤·스프린트에서 **아이디어에서 MVP까지** 가는 과정을, 팀이 따라갈 수 있는 **문서 템플릿**으로 정리한 레포지토리입니다.

기존에도 “문제 이해 → 아이디어 구체화 → 만들기” 순서로 MVP를 만드는 워크숍·스프린트 방식은 있었습니다. **vibe sprint**는 그 흐름을 바꾸지 않고, AI 에이전트(Cursor, Claude, Codex 등)와 함께 돌리기 쉽게 다듬은 버전입니다.

- 각 단계마다 **무엇을 할지·하지 말지**가 `docs/` 템플릿에 적혀 있습니다.
- 단계 문서마다 **Guide**와 **프롬프트 예시**가 있어, 팀 논의 내용을 에이전트에 넘겨 산출물을 채울 수 있습니다.
- 루트 **`AGENTS.md`** 에 **Sprint Master** 페르소나가 정의되어 있어, “지금 몇 단계인지·다음에 뭘 하면 되는지”를 에이전트에게 물어볼 수 있습니다.

## 이 레포에 있는 것

| 경로 | 역할 |
|------|------|
| `docs/01` ~ `docs/14` | 스프린트 14단계별 템플릿 (Guide·프롬프트 예시 포함) |
| `AGENTS.md` | Sprint Master — 단계 안내·실행 시 따를 페르소나 |
| `scripts/` | 특정 단계에서 쓰는 보조 스크립트 (해당 `docs/` 가이드 참고) |

단계별 상세 절차·명령어·체크리스트는 **README가 아니라 각 `docs/NN_*.md`** 에 있습니다.

## 스프린트는 세 구간으로 이어집니다

| 구간 | Step | 한 줄 요약 |
|------|------|-----------|
| **① 팀·문제 이해** | 01 → 07 | 누구와 무엇을, 지금 어떻게, 무엇이 아픈지·좋은지까지 넓게 수집 |
| **② 아이디어 구체화** | 08 → 11 | 질문·기능·화면·우리 서비스 흐름으로 좁힘 |
| **③ 만들기** | 12 → 14 | 스케치 합의 → 우선순위 → GitHub Issue로 구현 |

### 14단계별로 무엇을 하나

| Step | 절차 | 템플릿 |
|------|------|--------|
| 01 | 각자 아이디어 소개 및 팀빌딩 (대면) | [`docs/01_idea_teambuilding.md`](docs/01_idea_teambuilding.md) |
| 02 | 팀 캔버스 — 역할·목표·규칙 합의 | [`docs/02_team_canvas.md`](docs/02_team_canvas.md) |
| 03 | 서비스 목적·타겟·핵심 가치 정리 (아직 하나로 결정하지 않음) | [`docs/03_service_goal_target_value.md`](docs/03_service_goal_target_value.md) |
| 04 | **기존** 고객 여정 — 사용자가 목적을 지금 어떻게 달성하는가 | [`docs/04_existing_customer_journey.md`](docs/04_existing_customer_journey.md) |
| 05 | 여정에서 Pain Point / Wow Point 추출 | [`docs/05_pain_wow_points.md`](docs/05_pain_wow_points.md) |
| 06 | Wow 뒤 숨은 전제를 검증하는 질문 만들기 | [`docs/06_hypothesis_questions.md`](docs/06_hypothesis_questions.md) |
| 07 | 키워드로 팀 생각 시각화 (워드클라우드) | [`docs/07_word_cloud.md`](docs/07_word_cloud.md) |
| 08 | "어떻게 하면 ~" 질문으로 메커니즘 구체화 | [`docs/08_how_might_we_questions.md`](docs/08_how_might_we_questions.md) |
| 09 | 논의에서 나온 기능을 **전부** 나열 (우선순위·제외 없음) | [`docs/09_feature_list.md`](docs/09_feature_list.md) |
| 10 | 기능(F-xx)을 페이지별로 배치 (제외 없음) | [`docs/10_page_routing_split.md`](docs/10_page_routing_split.md) |
| 11 | **우리 서비스** 고객 여정 맵 | [`docs/11_customer_journey_map.md`](docs/11_customer_journey_map.md) |
| 12 | 각자 AI로 스케치 → 공유·합의, 최종 스케치만 기록 (대면 워크숍) | [`docs/12_sketch_and_decision.md`](docs/12_sketch_and_decision.md) |
| 13 | 기능(F-xx)별 1~4순위·스펙 아웃 | [`docs/13_priority_matrix.md`](docs/13_priority_matrix.md) |
| 14 | `docs/13` 기준 Issue 일괄 등록, 팀원이 Issue 단위로 구현 | [`docs/14_development.md`](docs/14_development.md) |

Step 01은 문서 작성 없이 대면으로 진행합니다. **본격적인 스프린트 문서는 `docs/03`부터** 채웁니다. Step 14 이후 진행 상황은 **GitHub Issues**가 기준입니다.

**헷갈리기 쉬운 점:** Step 04는 *지금 세상*의 여정, Step 11은 *우리가 만들 서비스* 여정입니다. Step 09·10에서는 기능을 빼지 않고 모으고 배치하고, **Step 13에서 비로소** 우선순위를 정합니다.

## 처음 시작하기

1. GitHub에서 **Use this template** → **Create a new repository** 로 팀 프로젝트 레포를 만듭니다. (본인 소유 레포는 fork가 되지 않으므로 template 사용을 권장합니다. 다른 사람 레포라면 fork도 가능합니다.)
2. 새 레포를 clone한 뒤, 팀빌딩·팀 캔버스(Step 01·02)를 마칩니다.
3. **`docs/03_service_goal_target_value.md`** 를 열고, 상단 **Guide**를 읽은 다음 **프롬프트 예시**를 에이전트에 붙여 논의 내용을 채웁니다.
4. **`docs/04` → … → `docs/14`** 순서로 진행합니다. 단계를 건너뛰지 않는 것이 좋습니다 (예: 기능 나열 전에 우선순위를 정하지 않음).
5. 막히면 에이전트에게 “지금 Step 몇이야? 뭘 하면 돼?”라고 물어보세요. `AGENTS.md`의 Sprint Master가 해당 `docs/` 파일을 가리켜 안내합니다.

## 템플릿으로 만든 프로젝트 예시

| 프로젝트 | 설명 |
|----------|------|
| [da-in/vibe-chord](https://github.com/da-in/vibe-chord) | 비전문가도 직관적인 인터페이스로 코드 진행을 탐색·학습·만드는 웹 도구. `docs/` 스프린트 산출물과 `web/` 구현 코드가 함께 있습니다. |

위 레포는 이 템플릿에서 **Use this template** 으로 만든 프로젝트입니다. 팀마다 독립 레포를 두고 `docs/`를 채운 뒤 Step 14에서 Issue·코드를 쌓아 가면 됩니다.

## 에이전트 친화적으로 바뀐 점

- **입력·출력이 문서로 고정**되어, 팀 논의 → 마크다운 → 다음 단계 입력이 이어집니다.
- **단계마다 프롬프트 예시**가 있어, 매번 지시문을 새로 쓰지 않아도 됩니다.
- **Sprint Master**(`AGENTS.md`)가 14단계 순서와 “이 단계에서 하지 말 것”을 알고 있어, 조기에 범위를 자르거나 단계를 건너뛰는 실수를 줄입니다.
- Step 14에서 **`docs/13` 기준으로 Issue를 등록**해, 구현도 에이전트·팀원이 Issue 단위로 나눠 진행할 수 있습니다.
