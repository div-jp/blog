var count = 0;
function clickMe(e) {
    if (count++ % 2 == 0) {
        e.textContent = "○";
    } else {
        e.textContent = "×";
    }
}
 





