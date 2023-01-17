$ wget -r l1 htttp://example.com/ 
"""재귀적으로 내려받기
재귀적으로 내려받을 때는 보통 5가지를 순회
5단계는 매우 깊고, 내려받는 데 시간도 꽤 걸리는 정도이기에 -l1옵션을 사용해 몇 번째 단계까지 순회할 것인지 확인
예를 들어 -l1이라고 지정하면 1단계 까지만 
"""

$ wget -r -l1 -w3 http://example.com/
"""
-w옵션은 '내려받기를 시작하기 전에 지정한 시간만큼 대기'하게 만드는 옵션
-w3이라고 지정하면 3초 간격으로 내려 받음
