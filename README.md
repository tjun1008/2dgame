# 2d게임 프로그래밍 게임 중간 발표
  
## 1.게임 소개
   - 다양하게 구성된 지형 내에서 몬스터를 쓰러트려가고 스테이지를 클리어해가며 보스를 잡는것이 목표   



## 2.현재 진행사항
   - 1주차 : 캐릭터, 맵 디자인 소스구하기, 게임 세부 디자인 (100%)
   - 2주차 : 맵 구현하기 1,2,3 스테이지 (100%)
   - 3주차 : 맵 구현하기 4(보스) 스테이지, 몬스터 배치 (70%)
   - 4주차 : 캐릭터 움직임 공격 구현 (100%)
   - 5주차 : 충돌처리, 몬스터가 죽으면 나오는 보상처리 (90%)
   - 6주차 : 보스 몬스터 구현, 보스몬스터 스테이지의 구현 상세화 (0%)
   - 7주차 : 포탈과 그 외의 추가구현, 게임 실행후 문제점 발견 (50%) 포탈 구현
   - 8주차 : 게임 문제점 보완 
   
   
   
## 3. git commit 
![1](https://github.com/tjun1008/2dgame/blob/master/%EC%88%98%EC%97%85%EB%82%B4%EC%9A%A9/image/2d%20%EC%BB%A4%EB%B0%8B.PNG?raw=true)
   - 전체 커밋수   
   
![2](https://github.com/tjun1008/2dgame/blob/master/%EC%88%98%EC%97%85%EB%82%B4%EC%9A%A9/image/2%EC%A3%BC%EC%B0%A8.PNG?raw=true)
   - 2주차
   
![3](https://github.com/tjun1008/2dgame/blob/master/%EC%88%98%EC%97%85%EB%82%B4%EC%9A%A9/image/4%EC%A3%BC%EC%B0%A8.PNG?raw=true)
   - 4주차 
   
![4](https://github.com/tjun1008/2dgame/blob/master/%EC%88%98%EC%97%85%EB%82%B4%EC%9A%A9/image/5%EC%A3%BC%EC%B0%A8.PNG?raw=true)
   - 5주차
   
![5](https://github.com/tjun1008/2dgame/blob/master/%EC%88%98%EC%97%85%EB%82%B4%EC%9A%A9/image/6%EC%A3%BC%EC%B0%A8.PNG?raw=true)
   - 6주차 
   
![6](https://github.com/tjun1008/2dgame/blob/master/%EC%88%98%EC%97%85%EB%82%B4%EC%9A%A9/image/7%EC%A3%BC%EC%B0%A8.PNG?raw=true)
   - 7주차 
   
   
## 4. class 구성정보

![7](https://github.com/tjun1008/2dgame/blob/master/%EC%88%98%EC%97%85%EB%82%B4%EC%9A%A9/image/2d%20%ED%81%B4%EB%9E%98%EC%8A%A4.PNG?raw=true)
   - 전체적으로 title,logo state, game state, player 클래스, stage 클래스, monster(zombie) 클래스, (fire)ball 클래스가 있다
   
![8](https://github.com/tjun1008/2dgame/blob/master/%EC%88%98%EC%97%85%EB%82%B4%EC%9A%A9/image/%EC%BA%A1%EC%B2%98.PNG?raw=true)
   - 게임 흐름으로는 logo title state를 진행한다음 main스테이지인 game 스테이지로 가서 map (stage1)과 프레임워크의 월드를 생성하고 드로우하고 업데이트한다.
   
![9](https://github.com/tjun1008/2dgame/blob/master/%EC%88%98%EC%97%85%EB%82%B4%EC%9A%A9/image/map1.PNG?raw=true)
   - stage 구성은 stage1,2,3,4를 구성한 다음 포탈에 충돌할때마다 map의 변수를 바꿔서 현재있던 stage를 딜리트하고 다음 stage를 그려내는 방식으로 한다.
   - portal과 몬스터는 모두 스테이지에 그리고 상호작용한다. 따라서 포탈과 몬스터는 스테이지마다 바뀌게된다
   
![10](https://github.com/tjun1008/2dgame/blob/master/%EC%88%98%EC%97%85%EB%82%B4%EC%9A%A9/image/character1.PNG?raw=true)
![11](https://github.com/tjun1008/2dgame/blob/master/%EC%88%98%EC%97%85%EB%82%B4%EC%9A%A9/image/character2.PNG?raw=true)
   - player은 키를 누를때마다 state를 바꿔서 (idle,running,up,down) state마다 상태를 업데이트하는 방식으로 진행된다
   
![12](https://github.com/tjun1008/2dgame/blob/master/%EC%88%98%EC%97%85%EB%82%B4%EC%9A%A9/image/ball1.PNG?raw=true)
   - player 각 스테이트에서 스페이스바를 누르면 파이어볼을 생성하는 함수를 만들고 gamestate에서 업데이트한다 파이어볼이 스테이지밖에서 나가면 삭제하는 방식으로 인해 메모리를 아낀다
   
![13](https://github.com/tjun1008/2dgame/blob/master/%EC%88%98%EC%97%85%EB%82%B4%EC%9A%A9/image/monster1.PNG?raw=true)
   - stage에서 몬스터를 초기화시키고 몬스터 스테이트에서 ball object를 불러 두 객체를 충돌검사시켜 충돌 확인되면 몬스터가 죽는 모션을하고 delete한다  
   

## 4. 다뤘으면 하는것
   - 아이템을 얻어 저장하는기능?을 했으면 좋겠다
   
   
   

   
   
