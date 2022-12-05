P=None
Q=chr
R=ord
S=list
M='.'
N=' '
J=''
G=int
H=range
F=print
E=str
C=len
import hashlib as T
from textwrap import wrap as L
def A(jsont,key,locallaw,mode):
	A=locallaw;B=jsont
	if mode==0:return D(B,key,A)
	elif mode==-1:return I(B,key,A)
def D(jsont,key,locallaw):
	D=P;D=jsont
	for F in H(locallaw):D=T.sha256(D.encode()).hexdigest()
	D=S(D)
	for F in H(C(D)):D[F]=R(D[F])
	A=J
	for K in D:A+=E(K)
	A=A[::-1];A=L(A,3)
	for I in H(C(A)):A[I]=G(A[I]);A[I]+=key;A[I]=E(A[I])
	A=J.join(A);B=J
	for K in D:A+=E(K)
	A=A[::-1];A=L(A,3)
	for F in H(C(A)):
		if G(A[F])<=254 and G(A[F])>=33:B+=E(Q(G(A[F])))
		else:B+=E(A[F])
	B=B.replace(N,M)
	while C(B)!=128:
		if C(B)>=129:O=C(B)-128;B=B[O:]
		elif C(B)<=127:B=B+B
	B=B.replace(N,M);return B
def I(jsont,key,locallaw):
	D=P;D=jsont
	for I in H(locallaw):D=T.sha256(D.encode()).hexdigest()
	D=S(D);F('a: {}'.format(D))
	for I in H(C(D)):D[I]=R(D[I])
	F('b: {}'.format(D));A=J
	for O in D:A+=E(O)
	A=A[::-1];F('c: {}'.format(A));A=L(A,3);F('d: {}'.format(A))
	for K in H(C(A)):A[K]=G(A[K]);A[K]+=key;A[K]=E(A[K])
	F('e: {}'.format(A));A=J.join(A);F('f: {}'.format(A));B=J
	for O in D:A+=E(O)
	A=A[::-1];A=L(A,3);F('g: {}'.format(A))
	for I in H(C(A)):
		if G(A[I])<=254 and G(A[I])>=33:B+=E(Q(G(A[I])))
		else:B+=E(A[I])
	F('h: {}'.format(B))
	while C(B)!=128:
		if C(B)>=129:U=C(B)-128;B=B[U:]
		elif C(B)<=127:B=B+B
	F('i: {}'.format(B));B=B.replace(N,M);return B