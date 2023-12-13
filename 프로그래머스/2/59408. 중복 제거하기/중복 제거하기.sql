-- 코드를 입력하세요
-- null 체크 방법 : is null 등. SQLD에서 했었는데 까먹었네;
-- SELECT distinct count(NAME)
-- FROM ANIMAL_INS
-- WHERE NAME is not null

SELECT count(DISTINCT NAME)
FROM ANIMAL_INS
WHERE NAME is not null;