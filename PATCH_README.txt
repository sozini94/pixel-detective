픽셀 탐정 v1.4 사건별 아이콘 경로 패치

기존 프로젝트 폴더에 cases/ 및 assets/ 폴더를 덮어쓰세요.
사건 JSON의 clues[].icon은 예: case-01/cctv 처럼 저장됩니다.
기존 app.js의 image('icons', c.icon) 함수가 assets/icons/case-01/cctv.png 경로를 만듭니다.
기존 아이콘 파일과 JavaScript는 교체할 필요가 없습니다.
검증: 사건 10개, 단서 이미지 131개 파일 존재 확인.
