%global tl_name babel-italian
%global tl_revision 77371

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5.02
Release:	%{tl_revision}.1
Summary:	Babel support for Italian text
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/italian
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-italian.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-italian.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-italian.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides language definitions for use in babel.

