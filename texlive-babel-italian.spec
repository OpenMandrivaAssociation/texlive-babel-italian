# revision 32213
# category Package
# catalog-ctan /macros/latex/contrib/babel-contrib/italian
# catalog-date 2013-11-22 18:28:56 +0100
# catalog-license lppl1.3
# catalog-version 1.3f
Name:		texlive-babel-italian
Version:	1.3f
Release:	1
Summary:	Babel support for Italian text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/italian
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-italian.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-italian.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-italian.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides language definitions for use in babel.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-italian/italian.ldf
%doc %{_texmfdistdir}/doc/generic/babel-italian/italian.pdf
#- source
%doc %{_texmfdistdir}/source/generic/babel-italian/italian.dtx
%doc %{_texmfdistdir}/source/generic/babel-italian/italian.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
