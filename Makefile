CLANGVERSION=3.4

autodoc_c/clang: clang-$(CLANGVERSION)
	cp -r clang-$(CLANGVERSION)/bindings/python/clang autodoc_c/clang/
	find autodoc_c/clang -name "*.py" -exec sed -i "" "s/^import clang$$/from autodoc_c import clang/" {} \;
	find autodoc_c/clang -name "*.py" -exec sed -i "" "s/^import clang.enumerations$$/import autodoc_c.clang.enumerations; from autodoc_c import clang/" {} \;

clang-$(CLANGVERSION): clang-$(CLANGVERSION).src.tar.gz
	tar -xzf clang-$(CLANGVERSION).src.tar.gz

clang-$(CLANGVERSION).src.tar.gz:
	curl http://llvm.org/releases/$(CLANGVERSION)/clang-$(CLANGVERSION).src.tar.gz -o clang-$(CLANGVERSION).src.tar.gz
