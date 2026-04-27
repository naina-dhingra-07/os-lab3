def fifo(pages, frames):
    memory = []
    queue = []
    faults = 0

    for page in pages:
        if page not in memory:
            faults += 1
            if len(memory) < frames:
                memory.append(page)
                queue.append(page)
            else:
                oldest = queue.pop(0)
                memory.remove(oldest)
                memory.append(page)
                queue.append(page)
    return faults


def lru(pages, frames):
    memory = []
    recent = []
    faults = 0

    for page in pages:
        if page not in memory:
            faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                lru_page = recent.pop(0)
                memory.remove(lru_page)
                memory.append(page)
        else:
            recent.remove(page)

        recent.append(page)

    return faults


def optimal(pages, frames):
    memory = []
    faults = 0

    for i in range(len(pages)):
        page = pages[i]

        if page not in memory:
            faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                future = pages[i+1:]
                index = []

                for m in memory:
                    if m in future:
                        index.append(future.index(m))
                    else:
                        index.append(float('inf'))

                replace = index.index(max(index))
                memory[replace] = page

    return faults


def mru(pages, frames):
    memory = []
    recent = []
    faults = 0

    for page in pages:
        if page not in memory:
            faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                mru_page = recent[-1]
                memory.remove(mru_page)
                memory.append(page)
        else:
            recent.remove(page)

        recent.append(page)

    return faults


def second_chance(pages, frames):
    memory = []
    ref_bit = []
    pointer = 0
    faults = 0

    for page in pages:
        if page in memory:
            ref_bit[memory.index(page)] = 1
        else:
            faults += 1
            if len(memory) < frames:
                memory.append(page)
                ref_bit.append(1)
            else:
                while True:
                    if ref_bit[pointer] == 0:
                        memory[pointer] = page
                        ref_bit[pointer] = 1
                        pointer = (pointer + 1) % frames
                        break
                    else:
                        ref_bit[pointer] = 0
                        pointer = (pointer + 1) % frames

    return faults


# ===== MAIN PROGRAM =====
frames = int(input("Enter number of frames: "))
pages = list(map(int, input("Enter page reference string: ").split()))

print("\nPage Reference String:", pages)

print("\nFIFO Page Faults:", fifo(pages, frames))
print("LRU Page Faults:", lru(pages, frames))
print("Optimal Page Faults:", optimal(pages, frames))
print("MRU Page Faults:", mru(pages, frames))
print("Second Chance Page Faults:", second_chance(pages, frames))