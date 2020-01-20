;;;; Question : https://www.youtube.com/watch?v=EuPSibuIKIg

(defun dot-product (p1 p2)
  "Compute cross product of two points"
  (-
   (* (car p1) (cadr p2))
   (* (car p2) (cadr p1))
   ))

(defun is-origin (p)
  "Check if point is the origin (0, 0)"
  (if (and (equalp 0 (car p))
	   (equalp 0 (cadr p)))
      t nil))

(defun is-orthogonal (v1 v2)
  "Check if v1 and v2 are orthogonal"
  (if (and (equal 0 (dot-product v1 v2))
	   (not (or (is-origin v1) (is-origin v2))))
      t nil))

(defun make-vector (p1 p2)
  "Make vector out of two points"
  (cons (- (car p2) (car p1))
	(- (cadr p2) (cadr p1))))

(defun is-right-rectangle (p1 p2 p3 p4)
  "Check if form defined by p1 p2 p3 p4 in this order is a rectangle"
  (if (and (is-orthogonal (make-vector p1 p2)
			  (make-vector p2 p3))
	   (is-orthogonal (make-vector p2 p3)
			  (make-vector p3 p4))
	   (is-orthogonal (make-vector p3 p4)
			  (make-vector p4 p1)))
      t nil))

(defun is-rectangle (p1 p2 p3 p4)
  "Check if form defined by p1 p2 p3 p4 is a rectangle"
  (or (is-right-rectangle p1 p2 p3 p4)
      (is-right-rectangle p2 p1 p3 p4)
      (is-right-rectangle p1 p2 p3 p4)))

(defun count-rectangles (&rest points)
  "Counts rectangles"
  (setf *count* 0)
  (setq points2 '(cdr points))
  (setq points3 '(cdr points2))
  (setq points4 '(cdr points3))
  (do list (p1 points)
    (do list (p2 points2)
      (do list (p3 points3)
	(do list (p4 points4)
	  (if (is-rectangle p1 p2 p3 p4)
	      (setf *count* (1+ *count*))
	      nil))
	(setq points4 '(cdr points4)))
      (setq points3 '(cdr points3)))
    (setq points2 '(cdr points2)))
  *count*)

(dot-product '(0 1) '(9 2))
(cdr '(1 2 3))
(make-vector '(2 3) '(4 5))

(< 2 3)
