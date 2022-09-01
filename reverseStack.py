def reverseStack(s):
    def insert(st, val):
        if not st:
            st.append(val)
        else:
            popped = st.pop()
            insert(st, val)
            st.append(popped)

    if not s:
        return None
    popped = s.pop()
    reverseStack(s)
    print(s)
    insert(s, popped)

    return s

reverseStack([1,2,3,4,5])