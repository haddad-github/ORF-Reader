frame1 = ['TTG', 'CAA', 'TTG', 'GAT', 'GAG', 'TTT', 'ACC', 'AGG', 'TCC', 'GAA', 'CTT', 'ATT', 'GGA', 'GGT', 'AAG', 'ATA', 'AAT', 'TAG', 'AAG']
frame2 = ['TGC', 'AAT', 'TGG', 'ATG', 'AGT', 'TTA', 'CCA', 'GGT', 'CCG', 'AAC', 'TTA', 'TTG', 'GAG', 'GTA', 'AGA', 'TAA', 'ATT', 'AGA', 'AG']
frame3 = ['GCA', 'ATT', 'GGA', 'TGA', 'GTT', 'TAC', 'CAG', 'GTC', 'CGA', 'ACT', 'TAT', 'TGG', 'AGG', 'TAA', 'GAT', 'AAA', 'TTA', 'GAA', 'G']

start = "ATG"
stop = ["TAA", "TGA", "TAG"]

for frame in [frame1, frame2, frame3]:
    if start not in frame:
        print("No genes in this frame")

    else:
     start_index = frame.index(start)
     stop_index = min(frame.index(i) for i in stop if i in frame)
     print("Gene:", "".join(frame[start_index:stop_index]))

