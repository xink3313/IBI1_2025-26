def read_fasta(filename):
    """读取 FASTA 文件，去除表头和换行符，返回纯氨基酸序列字符串"""
    with open(filename, 'r') as f:
        lines = f.readlines()
    # 拼接从第二行开始的所有序列，忽略 > 开头的表头
    sequence = "".join([line.strip() for line in lines[1:]])
    return sequence

def read_blosum62(filename):
    """读取 BLOSUM62 矩阵文件，将其转化为字典格式进行查表得分 [cite: 149]"""
    blosum = {}
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    header = []
    for line in lines:
        if not line.startswith("#") and line.strip():
            header = line.split()
            break
            
    for line in lines:
        if not line.startswith("#") and line.strip() and not line.startswith(" "):
            parts = line.split()
            aa1 = parts[0]
            scores = [int(x) for x in parts[1:]]
            for i, aa2 in enumerate(header):
                blosum[(aa1, aa2)] = scores[i]
    return blosum

def compare_sequences(seq1_name, seq1, seq2_name, seq2, matrix):
    """比较两条序列，计算百分比相似度 (Percentage Identity) 和 BLOSUM62 得分 [cite: 140, 150-154]"""
    if len(seq1) != len(seq2):
        print(f"Error: {seq1_name} and {seq2_name} lengths do not match!")
        return

    identical_aa = 0
    total_score = 0
    
    # 逐个比较氨基酸 [cite: 151-152]
    for i in range(len(seq1)):
        aa1 = seq1[i]
        aa2 = seq2[i]
        
        # 1. 计算有多少个氨基酸完全一致 [cite: 140]
        if aa1 == aa2:
            identical_aa += 1
            
        # 2. 查表获取 BLOSUM62 替换得分并累加 [cite: 153-154]
        # 如果遇到矩阵中没有的异常字符（如序列末尾的换行），默认给 0 分
        score = matrix.get((aa1, aa2), 0) 
        total_score += score

    # 计算相似度百分比 [cite: 140]
    percentage = (identical_aa / len(seq1)) * 100
    
    # 打印最终报告 [cite: 156-157]
    print(f"--- Alignment Output: {seq1_name} vs {seq2_name} ---")
    print(f"Percentage Identity: {percentage:.2f}% ({identical_aa}/{len(seq1)} amino acids)")
    print(f"Total BLOSUM62 Score: {total_score}")
    print("-" * 55)

# ==========================================
# 主程序执行区
# ==========================================
# 1. 读取所有的输入文件 [cite: 148-149]
human_seq = read_fasta("human_DLX5.fasta")
mouse_seq = read_fasta("mouse_DLX5.fasta")
random_seq = read_fasta("random_seq.fasta")
blosum_matrix = read_blosum62("blosum62.txt")

# 2. 执行所有三种两两配对的对比分析 [cite: 178]
compare_sequences("Human DLX5", human_seq, "Mouse DLX5", mouse_seq, blosum_matrix)
compare_sequences("Human DLX5", human_seq, "Random Sequence", random_seq, blosum_matrix)
compare_sequences("Mouse DLX5", mouse_seq, "Random Sequence", random_seq, blosum_matrix)