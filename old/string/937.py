class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        
        for log in logs:
            parsed = log.split()
            # 숫자 로그라면
            if parsed[1].isdigit():
                digit_logs.append(log)
            else: # 문자 로그라면
                letter_logs.append(log)
                
        sorted_letters = sorted(letter_logs, key=lambda x : (x.split()[1:], x.split()[0]))
        
        return sorted_letters + digit_logs
