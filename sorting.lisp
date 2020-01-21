(defun insert-sort-list (e l)
  (if (null l)
      (list e)
      (if (> e (car l))
	  (cons (car l) (insert-sort-list e (cdr l) ))
	  (cons e l))))

(defun select-sort (l sl)
  (if (null l)
      sl
      (if (listp l)
	  (select-sort (cdr l) (insert-sort-list (car l) sl))
	  (select-sort nil l))))

(defun bubble-sort (l)
  (if (null l)
      l
      (if (listp l)
	  (let ((head (car l)) (tail (cdr l)))
	    (if (listp tail)
		(if (< head (car tail))
		    (cons head (bubble-sort tail))))))))

(let ((l '(3 6 1 2 7 4 2 6 35 2)))
  (select-sort l nil)
  ;; (bubble-sort l)
  )

