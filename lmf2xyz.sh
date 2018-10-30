awk 'NR<=4 {print  "  Be ",$3,$4,$5}' xred >xxred
awk 'NR>4 && NR<=8  {print  "  Si ",$3,$4,$5}' xred >>xxred
awk 'NR>8 && NR<=16 {print  "  N     ",$3,$4,$5}' xred >>xxred
