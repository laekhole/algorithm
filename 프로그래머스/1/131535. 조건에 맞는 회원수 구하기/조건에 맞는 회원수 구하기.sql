-- 코드를 입력하세요
 -- 첫번째 답 : 틀림
 -- 간략 이유 : 조건절 제대로 확인 안 함.
 -- 상세 이유 : 조건절 2개임. 근데 '21년에 가입한 회원'을 누락
 -- SELECT count(*)
 -- FROM user_info
 -- WHERE age between 20 AND 29;

--  2번째 틀림. 에러
--  Every derived table must have its own alias
--  근데 이거 오라클로 셋팅 안하고 MySQL로 잡혀서 그랬던 거임
--  오라클로 셋팅하니까 다른 에러남

--  SELECT count(*)
--  FROM (
--      SELECT AGE
--      FROM user_info
--      WHERE JOINED >= 2021-01-01)
--  WHERE age between 20 AND 29;

--  3번째 틀림
--  ORA-01861: literal does not match format string
-- SELECT count(*)
-- FROM (
--     SELECT AGE
--     FROM user_info
--     WHERE JOINED >= 2021-01-01)
-- WHERE age between 20 AND 29;


-- 4번째 틀림
-- 괄호 빼먹음. 내가 그럼 그렇지...
-- SELECT count(*)
-- FROM (
--     SELECT AGE
--     FROM user_info
--     WHERE JOINED >= TO_DATE('2021-01-01','YYYY-MM-DD')
-- WHERE age between 20 AND 29;

    
SELECT COUNT(*)
FROM (
    SELECT USER_ID, AGE, JOINED
    FROM user_info
    WHERE JOINED >= TO_DATE('2021-01-01','YYYY-MM-DD') AND JOINED<TO_DATE('2022-01-01','YYYY-MM-DD')
    )
WHERE age between 20 AND 29;