vld1.16 {d2}, [r1]!
vmull.s16 q1, d2, d0[0]
vaddw.s16 q1, q1, d1
vqrshrun.s32 d2, q1, #8
vst1.16 {d2}, [r0]!