# namespace-package-poc
Example of namespace_packages

To install one namespace and its dependencies

```
# will only install formatting_utills and its requirements
pip install "git+https://github.com/isaaclubanko/namespace-package-poc.git@0.0.3#egg=0.0.3&subdirectory=formatting_utils"
```