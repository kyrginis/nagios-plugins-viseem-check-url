PKGNAME=nagios-plugins-viseem-check-url
SPECFILE=${PKGNAME}.spec
FILES=check_url.py ${SPECFILE}

PKGVERSION=$(shell grep -s '^Version:' $(SPECFILE) | sed -e 's/Version:\s*//')

srpm: dist
	rpmbuild -ts --define='dist .el6' ${PKGNAME}-${PKGVERSION}.tar.gz

rpm: dist
	rpmbuild -ta ${PKGNAME}-${PKGVERSION}.tar.gz

dist:
	rm -rf dist
	mkdir -p dist/${PKGNAME}-${PKGVERSION}
	cp -pr ${FILES} dist/${PKGNAME}-${PKGVERSION}/
	tar zcf dist/${PKGNAME}-${PKGVERSION}.tar.gz -C dist ${PKGNAME}-${PKGVERSION}
	mv dist/${PKGNAME}-${PKGVERSION}.tar.gz .
	rm -rf dist

sources: dist

clean:
	rm -rf ${PKGNAME}-${PKGVERSION}.tar.gz
	rm -rf dist
