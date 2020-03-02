%module (package="swig_example")structs

%{
#define SWIG_FILE_WITH_INIT
#include "c/structs.h"
%}

%include "c/structs.h"

%extend CPoint {
	CPoint() {
		CPoint *p;
		p = (CPoint *) malloc(sizeof(CPoint));
		p->x = 0;
		p->y = 0;
		return p;
	}
	CPoint(double x, double y) {
		CPoint *p;
		p = (CPoint *) malloc(sizeof(CPoint));
		p->x = x;
		p->y = y;
		return p;
	}
	~CPoint() {
		free($self);
	}
}

%extend CRectangle {
	CRectangle() {
		CRectangle *r;
		r = (CRectangle *) malloc(sizeof(CRectangle));
		r->top_left.x = 0;
		r->top_left.y = 0;
		r->bottom_right.x = 0;
		r->bottom_right.y = 0;
		return r;
	}
	CRectangle(CPoint top_left, CPoint bottom_right) {
		CRectangle *r;
		r = (CRectangle *) malloc(sizeof(CRectangle));
		r->top_left = top_left;
		r->bottom_right = bottom_right;
		return r;
	}
	~CRectangle() {
		free($self);
	}
}