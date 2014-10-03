PKGNAME=ar-release
SPECFILE=${PKGNAME}.spec
PKG_FILES=src/*
FILES=${SPECFILE} ${PKG_FILES}

PKGVERSION=$(shell grep -s '^Version:' $(SPECFILE) | awk '{print $$2}')


sources: ${FILES}
	rm -rf dist
	mkdir -p dist/${PKGNAME}-${PKGVERSION}
	cp -pr ${FILES} dist/${PKGNAME}-${PKGVERSION}/.
	cd dist ; tar cfz ../${PKGNAME}-${PKGVERSION}.tar.gz ${PKGNAME}-${PKGVERSION}
	rm -rf dist


clean:
	rm -rf ${PKGNAME}-${PKGVERSION}.tar.gz
	rm -rf dist
