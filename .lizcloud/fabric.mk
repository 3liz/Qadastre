#
# Makefile for building/packaging qgis for 3liz
#

ifndef FABRIC
FABRIC:=$(shell [ -e .fabricrc ] && echo "fab -c .fabricrc" || echo "fab")
endif

VERSION=$(shell ./metadata_key ../cadastre/metadata.txt version)

main:
	echo "Makefile for packaging infra components: select a task"

PACKAGE=qgis3_cadastre
FILES = ../cadastre/composers ../cadastre/server ../cadastre/forms ../cadastre/icons ../cadastre/interface ../cadastre/scripts ../cadastre/styles ../cadastre/templates ../cadastre/*.py ../cadastre/icon.png ../cadastre/metadata.txt

build2/cadastre:
	@rm -rf build2/cadastre
	@mkdir -p build2/cadastre


.PHONY: package
package: build2/cadastre
	@echo "Building package $(PACKAGE)"
	@cp -rLp $(FILES) build2/cadastre/
	$(FABRIC) package:$(PACKAGE),versiontag=$(VERSION),files=cadastre,directory=./build2

