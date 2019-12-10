;;;; Question : https://www.youtube.com/watch?v=EuPSibuIKIg

(defun dot-product (p1 p2)
  "Compute cross product of two points"
  (+
   (* (car p1) (car p2))
   (* (cadr p1) (cadr p2))
   ))

(defun is-origin (p)
  "Check if point is the origin (0, 0)"
  (if (and (equalp 0 (car p))
	   (equalp 0 (cadr p)))
      t nil))

(defun is-orthogonal (v1 v2)
  "Check if v1 and v2 are orthogonal"
  (if (equal 0 (dot-product v1 v2))
	t nil))

(defun count-rectangles (&rest points)
  "Counts rectangles"
  (setf *count* 0)
  (do list (p1 points)
    (do list (p2 points)
      (if ))))
