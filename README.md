# 🦁 TalkieTown US (토키타운 US)
> **어린이를 위한 미국 실생활 100% 구어체 영어 회화 웹 게임**

---

## 1. 개요 (Overview)
**TalkieTown US**는 딱딱하고 어색한 교과서식 영어("How are you? I am fine, thank you.")에서 벗어나, 미국 현지 또래 아이들과 일상생활에서 실제로 매일 사용하는 **진짜 구어체(Real Spoken American English & Idioms)**를 흥미진진한 상황극(Role-Playing)으로 체득할 수 있도록 설계된 웹 기반 에듀테인먼트 게임입니다.

---

## 2. 주요 기능 및 특징 (Key Features)

### 🎨 1. 2가지 선택형 비주얼 테마 (Dual Themes)
- **Theme 1: Playful Cartoon (동글동글 캐주얼 카툰)**: 사자 레오, 펭귄 페니 등 귀여운 동물 캐릭터와 파스텔톤 애니메이션.
- **Theme 2: Comic Pop-Art (아메리칸 코믹스/웹툰)**: 미국 만화책 스타일의 볼드한 외곽선(`border: 3px solid #111827`)과 팝아트 말풍선, 역동적 컷씬 연출.
- 상단 토글 버튼으로 실시간 원클릭 전환 가능.

### 🎙️ 2. 어린이 발화 맞춤형 STT & 퍼지 매칭 엔진 (Levenshtein Matching)
- **3단계 텍스트 정규화**: 구두점 제거 및 아동 구어체 단축형(`wanna` ↔ `want to`, `im` ↔ `i am`, `its` ↔ `it is`, `fr` ↔ `for real` 등) 자동 전처리.
- **레벤슈타인 편집 거리(Levenshtein Distance)** 기반 유사도(0~100%) 실시간 판정:
  - **90% 이상**: ⭐⭐⭐ Perfect! (만점 효과음 및 폭죽)
  - **70% ~ 89%**: ⭐⭐ Great Job! (합격 차임 및 칭찬 피드백)
  - **70% 미만**: 부드러운 저자극 버저 후 원어민 모델 발음(0.7x) 자동 재생 안내.
- **테스트 시뮬레이션**: 마이크가 없는 PC 환경을 위한 '발화 성공 시뮬레이션' 버튼 기본 내장.

### 🔊 3. 제로 의존성 Web Audio API 사운드 신디사이저
- 외부 mp3 파일 없이 순수 브라우저 오디오 발진기(Oscillator)로 무지연 출력:
  - **정답 차임**: Sine/Triangle 523Hz~1047Hz 경쾌한 4음 아르페지오
  - **연속 콤보 보너스**: 3연속 이상 정답 시 빠른 상승 아르페지오
  - **버블 터치 피드백**: 버튼 및 카드 터치 시 귀여운 버블 팝(Pop) 효과음
  - **사운드 On/Off 토글**: 조용한 도서관/교실에서도 걱정 없는 상단 음소거 버튼 제공.

### 🐢 4. 고품질 Web Speech API TTS 발화 엔진 & 2단계 속도 조절
- **원어민 프리미엄 보이스 자동 선택**: OS 언어 설정에 영향받지 않고 미국 원어민 음성(`Google US English`, `Natural`, `Samantha`, `Jenny` 등)을 자동 바인딩하여 정확한 음소/연음 재생.
- **순차 대화 체이닝 (Sequential Speech Chaining)**: 선택지 발화 후 NPC 리액션이 겹치거나 잘리지 않고 자연스러운 350ms 대화 호흡으로 연속 재생.
- **크로미움 GC 조기 수거 방지**: 긴 문장도 중간 끊김 없이 매끄럽게 끝까지 재생.
- **2단계 발음 속도 토글**: 상단 `[🐰 Normal (0.92x)]` ↔ `[🐢 Slow (0.72x)]` 버튼을 통해 영어가 서툰 저학년 아동도 또렷하게 청취 가능.

### 🚀 5. 4개 연령대별 40개 멀티턴(Multi-turn) 에피소드 & 최고빈도 기본동사·구동사 커리큘럼 (총 260턴)
- **실전 회화의 핵심, 원어민 필수 기본동사 & 구동사 최고빈도 전면 탑재**: 모든 에피소드에 걸쳐 미국 원어민들이 매일 쓰는 핵심 기본동사(`get`, `take`, `have`, `make`, `put`, `keep`, `give`, `let`, `go`, `come`, `turn`, `run`, `hold`, `call` 등)와 최고빈도 생활 구동사(`put on`, `put back`, `put away`, `get off`, `get in`, `get going`, `get in line`, `pick up`, `pick out`, `clean up`, `watch out`, `hold on`, `hold up`, `come on`, `get on`, `hang on`, `hang out`, `eat up`, `give up`, `give back`, `throw away`, `make sure`, `make room`, `hurry up`, `count on`, `turn off`, `turn up`, `fill up`, `back up`, `keep it up`, `keep running`, `pull up`, `hit up`, `check out`, `chill out`, `wrap up`, `calm down`, `try on`, `point out`, `head out`, `hit the road` 등)를 유기적으로 녹여냈습니다.
- **연령대 발달 단계별 차등 확장 연속 티키타카**: 단발성 퀴즈가 아닌 기승전결이 살아있는 실전 스토리라인으로 대화가 이어집니다 (상황 진입 ➔ 플레이어 발화 ➔ NPC 반응 대사 & TTS ➔ 전개/협상 ➔ 기본동사/구동사 액션 ➔ 마무리 티키타카 ➔ 에피소드 클리어).
- **Tier 1 (만 6~8세 / 저학년 10개 에피소드, 50턴 / 에피소드당 5턴)**: 모래성 감탄, 놀이터 술래잡기, 간식 나누기, 블록 탑, 크레파스 실수, 미끄럼틀 양보, 잃어버린 스티커, 왕 비눗방울, 종이비행기 날리기, 하교 작별 인사.
- **Tier 2 (만 9~10세 / 중학년 10개 에피소드, 60턴 / 에피소드당 6턴)**: 타이어 그네 찜, 급식실 자리 맡기, 피구 경기 작전, 만화책 스포 방어, 쉬는 시간 달리기, 포켓몬 카드 교환, 깜빡한 숙제 위기, 아케이드 재도전, 레이저 태그 생일 파티, 비밀 아지트 규칙.
- **Tier 3 (만 11~13세 / 고학년 10개 에피소드, 70턴 / 에피소드당 7턴)**: 방과 후 버블티, 스케이트보드 킥플립, 화산 과학 실험, 민트 후드티 쇼핑, 이어폰 명곡 공유, 사물함 비번 까먹음, 급식 미스터리 고기, 노을 자전거 라이딩, 시험 전날 벼락치기, 캠핑 불멍 스모어.
- **Tier 4 (만 14~16세 / 청소년 하이틴 10개 에피소드, 80턴 / 에피소드당 8턴)**: 락커룸 농구 내기, 방과 후 썰 풀기, 금요일 풋볼 경기, 복도 드립 대잔치, 틱톡 댄스 바이럴, 기말고사 끝 해방, 관중석 비밀 고민, 콘서트 맨 앞줄 티켓팅, 빈티지 룩 꿀득템, 방학 카운트다운.
- 총 **40개 에피소드, 260개의 연속 발화 턴**이 모듈러 데이터베이스(`scenarios.js`)로 완벽 구축.

### 🏆 6. 티어 정복 축하 모달 (Level Master Trophy)
- 각 연령대의 10개 에피소드를 모두 정복하면 누적 별점과 최고 콤보(Streak)를 집계하는 축하 팝업이 노출되며, 자동으로 다음 연령대 레벨로 원클릭 도전 가능.

---

## 3. 실행 방법 (Setup & Usage)

별도의 복잡한 패키지 설치 없이, 웹 브라우저와 기본 Python만 있으면 즉시 실행 가능합니다.

### 🪟 Windows 사용자
1. 프로젝트 폴더에서 **`run.bat`** 파일을 더블 클릭합니다.
2. 로컬 웹 서버(`http://localhost:3000`)가 구동되며 기본 웹 브라우저가 자동으로 실행됩니다.

### 🐧 Linux / macOS 사용자
1. 터미널을 열고 다음 명령어를 실행합니다:
   ```bash
   chmod +x run.sh
   ./run.sh
   ```

---

## 4. Vercel 배포 가이드 (Deployment to Vercel)

본 프로젝트는 Vercel의 정적 호스팅 및 자동 HTTPS 환경에 100% 최적화되어 있습니다.

1. 본 프로젝트 코드를 본인의 **GitHub 저장소**에 푸시합니다.
2. [Vercel 대시보드](https://vercel.com)에 로그인 후 **"Add New Project"**를 누르고 해당 저장소를 선택합니다.
3. 빌드 설정(Build Settings) 변경 없이 **"Deploy"**를 클릭하면 끝!
4. 발급된 `https://your-app.vercel.app` 링크로 접속하면 태블릿과 모바일에서도 마이크 음성 인식이 즉시 동작합니다.

---

## 5. 트러블슈팅 (Troubleshooting)

| 현상 | 원인 및 해결 방법 |
| :--- | :--- |
| **마이크 음성 인식이 안 돼요** | 브라우저 주소창 왼쪽의 자물쇠/설정 아이콘을 눌러 **'마이크 권한'**을 '허용'으로 변경해주세요. `file://` 직접 실행 시 브라우저 보안으로 마이크가 차단될 수 있으므로 반드시 `run.bat`을 통해 `http://localhost:3000`으로 접속해 주세요. |
| **음성 인식이 어려운 환경이에요** | 상단 메뉴의 **`[🎙️ Voice Mode]`** 버튼을 클릭하여 **`[👆 Touch Mode]`**로 전환하시면 터치나 클릭만으로 모든 게임을 즐길 수 있습니다. |
| **소리가 안 나요** | 브라우저의 소리가 음소거되어 있지 않은지 확인해 주세요. 최초 클릭 상호작용 이후 Web Audio API 사운드가 정상 출력됩니다. |

---

## 6. 설계 문서 및 에이전트 시스템 (Architecture & Agent Protocol)

- **[DESIGN_DRAFT.md](file:///C:/Users/tickl/PycharmProjects/english_game/DESIGN_DRAFT.md)**: 15개 씬의 상황별 대화 시나리오 및 SVG 일러스트 기획 초안
- **[DETAILED_SPECIFICATION.md](file:///C:/Users/tickl/PycharmProjects/english_game/DETAILED_SPECIFICATION.md)**: 데이터 모델(TypeScript/JSON), 게임 FSM 상태 머신, 퍼지 음성 매칭 알고리즘, 신디사이저 사양서
- **[AGENTS.md](file:///C:/Users/tickl/PycharmProjects/english_game/AGENTS.md)**: 5대 전문 에이전트 협업 프로토콜 및 5대 품질 게이트 (Quality Gates)

