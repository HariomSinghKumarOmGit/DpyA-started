

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])

        row_s, row_e = 0, n - 1
        col_s, col_e = 0, m - 1

        ans = []

        while len(ans) < m * n:
            # top row (left → right)
            for i in range(col_s, col_e + 1):
                ans.append(matrix[row_s][i])
            row_s += 1
            if len(ans) == m * n:
                break

            # right column (top → bottom)
            for i in range(row_s, row_e + 1):
                ans.append(matrix[i][col_e])
            col_e -= 1
            if len(ans) == m * n:
                break

            # bottom row (right → left)
            for i in range(col_e, col_s - 1, -1):
                ans.append(matrix[row_e][i])
            row_e -= 1
            if len(ans) == m * n:
                break

            # left column (bottom → top)
            for i in range(row_e, row_s - 1, -1):
                ans.append(matrix[i][col_s])
            col_s += 1

        return ans