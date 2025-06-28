### Frontend Scan Results (devopsfinal-frontend:latest)
```

Report Summary

┌─────────────────────────────────────────────┬────────┬─────────────────┐
│                   Target                    │  Type  │ Vulnerabilities │
├─────────────────────────────────────────────┼────────┼─────────────────┤
│ devopsfinal-frontend:latest (alpine 3.22.0) │ alpine │        0        │
└─────────────────────────────────────────────┴────────┴─────────────────┘
Legend:
- '-': Not scanned
- '0': Clean (no security findings detected)

```

### Backend Scan Results (devopsfinal-backend:latest)
```

Report Summary

┌──────────────────────────────────────────────────────────────────────────────────┬────────────┬─────────────────┐
│                                      Target                                      │    Type    │ Vulnerabilities │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┤
│ devopsfinal-backend:latest (debian 12.11)                                        │   debian   │       297       │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┤
│ usr/local/lib/python3.9/site-packages/MarkupSafe-3.0.2.dist-info/METADATA        │ python-pkg │        0        │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┤
│ usr/local/lib/python3.9/site-packages/blinker-1.9.0.dist-info/METADATA           │ python-pkg │        0        │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┤
│ usr/local/lib/python3.9/site-packages/click-8.1.8.dist-info/METADATA             │ python-pkg │        0        │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┤
│ usr/local/lib/python3.9/site-packages/flask-2.3.3.dist-info/METADATA             │ python-pkg │        0        │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┤
│ usr/local/lib/python3.9/site-packages/gunicorn-23.0.0.dist-info/METADATA         │ python-pkg │        0        │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┤
│ usr/local/lib/python3.9/site-packages/importlib_metadata-8.7.0.dist-info/METADA- │ python-pkg │        0        │
│ TA                                                                               │            │                 │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┤
│ usr/local/lib/python3.9/site-packages/itsdangerous-2.2.0.dist-info/METADATA      │ python-pkg │        0        │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┤
│ usr/local/lib/python3.9/site-packages/jinja2-3.1.6.dist-info/METADATA            │ python-pkg │        0        │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┤
│ usr/local/lib/python3.9/site-packages/packaging-25.0.dist-info/METADATA          │ python-pkg │        0        │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┤
│ usr/local/lib/python3.9/site-packages/pip-23.0.1.dist-info/METADATA              │ python-pkg │        1        │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┤
│ usr/local/lib/python3.9/site-packages/prometheus_client-0.17.1.dist-info/METADA- │ python-pkg │        0        │
│ TA                                                                               │            │                 │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┤
│ usr/local/lib/python3.9/site-packages/psutil-5.9.5.dist-info/METADATA            │ python-pkg │        0        │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┤
│ usr/local/lib/python3.9/site-packages/setuptools-58.1.0.dist-info/METADATA       │ python-pkg │        3        │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┤
│ usr/local/lib/python3.9/site-packages/werkzeug-3.1.3.dist-info/METADATA          │ python-pkg │        0        │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┤
│ usr/local/lib/python3.9/site-packages/wheel-0.45.1.dist-info/METADATA            │ python-pkg │        0        │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┤
│ usr/local/lib/python3.9/site-packages/zipp-3.23.0.dist-info/METADATA             │ python-pkg │        0        │
└──────────────────────────────────────────────────────────────────────────────────┴────────────┴─────────────────┘
Legend:
- '-': Not scanned
- '0': Clean (no security findings detected)


devopsfinal-backend:latest (debian 12.11)
=========================================
Total: 297 (UNKNOWN: 0, LOW: 270, MEDIUM: 18, HIGH: 8, CRITICAL: 1)

┌───────────────────────────┬─────────────────────┬──────────┬──────────────┬────────────────────────┬───────────────┬──────────────────────────────────────────────────────────────┐
│          Library          │    Vulnerability    │ Severity │    Status    │   Installed Version    │ Fixed Version │                            Title                             │
├───────────────────────────┼─────────────────────┼──────────┼──────────────┼────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ apt                       │ CVE-2011-3374       │ LOW      │ affected     │ 2.6.1                  │               │ It was found that apt-key in apt, all versions, do not       │
│                           │                     │          │              │                        │               │ correctly...                                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2011-3374                    │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ bash                      │ TEMP-0841856-B18BAF │          │              │ 5.2.15-2+b8            │               │ [Privilege escalation possible to other user than root]      │
│                           │                     │          │              │                        │               │ https://security-tracker.debian.org/tracker/TEMP-0841856-B1- │
│                           │                     │          │              │                        │               │ 8BAF                                                         │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ binutils                  │ CVE-2017-13716      │          │              │ 2.40-2                 │               │ binutils: Memory leak with the C++ symbol demangler routine  │
│                           │                     │          │              │                        │               │ in libiberty                                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2017-13716                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20673      │          │              │                        │               │ libiberty: Integer overflow in demangle_template() function  │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-20673                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20712      │          │              │                        │               │ libiberty: heap-based buffer over-read in d_expression_1     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-20712                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-9996       │          │              │                        │               │ binutils: Stack-overflow in libiberty/cplus-dem.c causes     │
│                           │                     │          │              │                        │               │ crash                                                        │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-9996                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2021-32256      │          │              │                        │               │ binutils: stack-overflow issue in demangle_type in           │
│                           │                     │          │              │                        │               │ rust-demangle.c.                                             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2021-32256                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2023-1972       │          │              │                        │               │ binutils: Illegal memory access when accessing a             │
│                           │                     │          │              │                        │               │ zer0-lengthverdef table                                      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-1972                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-53589      │          │              │                        │               │ binutils: objdump: buffer Overflow in the BFD library's      │
│                           │                     │          │              │                        │               │ handling of tekhex format...                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-53589                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-57360      │          │              │                        │               │ binutils: nm: potential segmentation fault when displaying   │
│                           │                     │          │              │                        │               │ symbols without version info                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-57360                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-0840       │          │              │                        │               │ binutils: GNU Binutils objdump.c disassemble_bytes           │
│                           │                     │          │              │                        │               │ stack-based overflow                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-0840                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1147       │          │              │                        │               │ binutils: GNU Binutils nm nm.c internal_strlen buffer        │
│                           │                     │          │              │                        │               │ overflow                                                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1147                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1148       │          │              │                        │               │ binutils: GNU Binutils ld ldelfgen.c link_order_scan memory  │
│                           │                     │          │              │                        │               │ leak                                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1148                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1149       │          │              │                        │               │ binutils: GNU Binutils ld xmalloc.c xstrdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1149                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1150       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_malloc memory leak    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1150                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1151       │          │              │                        │               │ binutils: GNU Binutils ld xmemdup.c xmemdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1151                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1152       │          │              │                        │               │ binutils: GNU Binutils ld xstrdup.c xstrdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1152                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1153       │          │              │                        │               │ binutils: GNU Binutils format.c bfd_set_format memory        │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1153                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1176       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │              │                        │               │ heap-based overflow                                          │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1176                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1178       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1178                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1179       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1179                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1180       │          │              │                        │               │ binutils: GNU Binutils ld elf-eh-frame.c                     │
│                           │                     │          │              │                        │               │ _bfd_elf_write_section_eh_frame memory corruption            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1180                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1181       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │              │                        │               │ memory corruption                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1181                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1182       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c                          │
│                           │                     │          │              │                        │               │ bfd_elf_reloc_symbol_deleted_p memory corruption             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1182                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-3198       │          │              │                        │               │ binutils: GNU Binutils objdump bucomm.c display_info memory  │
│                           │                     │          │              │                        │               │ leak                                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-3198                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5244       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c elf_gc_sweep memory      │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-5244                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5245       │          │              │                        │               │ binutils: GNU Binutils objdump debug.c debug_type_samep      │
│                           │                     │          │              │                        │               │ memory corruption                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-5245                    │
├───────────────────────────┼─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│ binutils-common           │ CVE-2017-13716      │          │              │                        │               │ binutils: Memory leak with the C++ symbol demangler routine  │
│                           │                     │          │              │                        │               │ in libiberty                                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2017-13716                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20673      │          │              │                        │               │ libiberty: Integer overflow in demangle_template() function  │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-20673                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20712      │          │              │                        │               │ libiberty: heap-based buffer over-read in d_expression_1     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-20712                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-9996       │          │              │                        │               │ binutils: Stack-overflow in libiberty/cplus-dem.c causes     │
│                           │                     │          │              │                        │               │ crash                                                        │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-9996                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2021-32256      │          │              │                        │               │ binutils: stack-overflow issue in demangle_type in           │
│                           │                     │          │              │                        │               │ rust-demangle.c.                                             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2021-32256                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2023-1972       │          │              │                        │               │ binutils: Illegal memory access when accessing a             │
│                           │                     │          │              │                        │               │ zer0-lengthverdef table                                      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-1972                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-53589      │          │              │                        │               │ binutils: objdump: buffer Overflow in the BFD library's      │
│                           │                     │          │              │                        │               │ handling of tekhex format...                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-53589                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-57360      │          │              │                        │               │ binutils: nm: potential segmentation fault when displaying   │
│                           │                     │          │              │                        │               │ symbols without version info                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-57360                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-0840       │          │              │                        │               │ binutils: GNU Binutils objdump.c disassemble_bytes           │
│                           │                     │          │              │                        │               │ stack-based overflow                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-0840                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1147       │          │              │                        │               │ binutils: GNU Binutils nm nm.c internal_strlen buffer        │
│                           │                     │          │              │                        │               │ overflow                                                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1147                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1148       │          │              │                        │               │ binutils: GNU Binutils ld ldelfgen.c link_order_scan memory  │
│                           │                     │          │              │                        │               │ leak                                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1148                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1149       │          │              │                        │               │ binutils: GNU Binutils ld xmalloc.c xstrdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1149                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1150       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_malloc memory leak    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1150                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1151       │          │              │                        │               │ binutils: GNU Binutils ld xmemdup.c xmemdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1151                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1152       │          │              │                        │               │ binutils: GNU Binutils ld xstrdup.c xstrdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1152                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1153       │          │              │                        │               │ binutils: GNU Binutils format.c bfd_set_format memory        │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1153                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1176       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │              │                        │               │ heap-based overflow                                          │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1176                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1178       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1178                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1179       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1179                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1180       │          │              │                        │               │ binutils: GNU Binutils ld elf-eh-frame.c                     │
│                           │                     │          │              │                        │               │ _bfd_elf_write_section_eh_frame memory corruption            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1180                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1181       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │              │                        │               │ memory corruption                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1181                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1182       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c                          │
│                           │                     │          │              │                        │               │ bfd_elf_reloc_symbol_deleted_p memory corruption             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1182                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-3198       │          │              │                        │               │ binutils: GNU Binutils objdump bucomm.c display_info memory  │
│                           │                     │          │              │                        │               │ leak                                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-3198                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5244       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c elf_gc_sweep memory      │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-5244                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5245       │          │              │                        │               │ binutils: GNU Binutils objdump debug.c debug_type_samep      │
│                           │                     │          │              │                        │               │ memory corruption                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-5245                    │
├───────────────────────────┼─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│ binutils-x86-64-linux-gnu │ CVE-2017-13716      │          │              │                        │               │ binutils: Memory leak with the C++ symbol demangler routine  │
│                           │                     │          │              │                        │               │ in libiberty                                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2017-13716                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20673      │          │              │                        │               │ libiberty: Integer overflow in demangle_template() function  │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-20673                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20712      │          │              │                        │               │ libiberty: heap-based buffer over-read in d_expression_1     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-20712                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-9996       │          │              │                        │               │ binutils: Stack-overflow in libiberty/cplus-dem.c causes     │
│                           │                     │          │              │                        │               │ crash                                                        │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-9996                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2021-32256      │          │              │                        │               │ binutils: stack-overflow issue in demangle_type in           │
│                           │                     │          │              │                        │               │ rust-demangle.c.                                             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2021-32256                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2023-1972       │          │              │                        │               │ binutils: Illegal memory access when accessing a             │
│                           │                     │          │              │                        │               │ zer0-lengthverdef table                                      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-1972                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-53589      │          │              │                        │               │ binutils: objdump: buffer Overflow in the BFD library's      │
│                           │                     │          │              │                        │               │ handling of tekhex format...                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-53589                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-57360      │          │              │                        │               │ binutils: nm: potential segmentation fault when displaying   │
│                           │                     │          │              │                        │               │ symbols without version info                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-57360                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-0840       │          │              │                        │               │ binutils: GNU Binutils objdump.c disassemble_bytes           │
│                           │                     │          │              │                        │               │ stack-based overflow                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-0840                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1147       │          │              │                        │               │ binutils: GNU Binutils nm nm.c internal_strlen buffer        │
│                           │                     │          │              │                        │               │ overflow                                                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1147                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1148       │          │              │                        │               │ binutils: GNU Binutils ld ldelfgen.c link_order_scan memory  │
│                           │                     │          │              │                        │               │ leak                                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1148                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1149       │          │              │                        │               │ binutils: GNU Binutils ld xmalloc.c xstrdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1149                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1150       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_malloc memory leak    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1150                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1151       │          │              │                        │               │ binutils: GNU Binutils ld xmemdup.c xmemdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1151                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1152       │          │              │                        │               │ binutils: GNU Binutils ld xstrdup.c xstrdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1152                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1153       │          │              │                        │               │ binutils: GNU Binutils format.c bfd_set_format memory        │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1153                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1176       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │              │                        │               │ heap-based overflow                                          │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1176                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1178       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1178                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1179       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1179                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1180       │          │              │                        │               │ binutils: GNU Binutils ld elf-eh-frame.c                     │
│                           │                     │          │              │                        │               │ _bfd_elf_write_section_eh_frame memory corruption            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1180                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1181       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │              │                        │               │ memory corruption                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1181                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1182       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c                          │
│                           │                     │          │              │                        │               │ bfd_elf_reloc_symbol_deleted_p memory corruption             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1182                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-3198       │          │              │                        │               │ binutils: GNU Binutils objdump bucomm.c display_info memory  │
│                           │                     │          │              │                        │               │ leak                                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-3198                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5244       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c elf_gc_sweep memory      │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-5244                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5245       │          │              │                        │               │ binutils: GNU Binutils objdump debug.c debug_type_samep      │
│                           │                     │          │              │                        │               │ memory corruption                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-5245                    │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ bsdutils                  │ CVE-2022-0563       │          │              │ 1:2.38.1-5+deb12u3     │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                           │                     │          │              │                        │               │ and chsh when compiled...                                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├───────────────────────────┼─────────────────────┤          ├──────────────┼────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ coreutils                 │ CVE-2016-2781       │          │ will_not_fix │ 9.1-1                  │               │ coreutils: Non-privileged session can escape to the parent   │
│                           │                     │          │              │                        │               │ session in chroot                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2016-2781                    │
│                           ├─────────────────────┤          ├──────────────┤                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2017-18018      │          │ affected     │                        │               │ coreutils: race condition vulnerability in chown and chgrp   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2017-18018                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5278       │          │              │                        │               │ coreutils: Heap Buffer Under-Read in GNU Coreutils sort via  │
│                           │                     │          │              │                        │               │ Key Specification                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-5278                    │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ cpp-12                    │ CVE-2022-27943      │          │              │ 12.2.0-14+deb12u1      │               │ binutils: libiberty/rust-demangle.c in GNU GCC 11.2 allows   │
│                           │                     │          │              │                        │               │ stack exhaustion in demangle_const                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-27943                   │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ curl                      │ CVE-2024-2379       │          │              │ 7.88.1-10+deb12u12     │               │ curl: QUIC certificate check bypass with wolfSSL             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-2379                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-0725       │          │              │                        │               │ libcurl: Buffer Overflow in libcurl via zlib Integer         │
│                           │                     │          │              │                        │               │ Overflow                                                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-0725                    │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ gcc-12                    │ CVE-2022-27943      │          │              │ 12.2.0-14+deb12u1      │               │ binutils: libiberty/rust-demangle.c in GNU GCC 11.2 allows   │
│                           │                     │          │              │                        │               │ stack exhaustion in demangle_const                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-27943                   │
├───────────────────────────┤                     │          │              │                        ├───────────────┤                                                              │
│ gcc-12-base               │                     │          │              │                        │               │                                                              │
│                           │                     │          │              │                        │               │                                                              │
│                           │                     │          │              │                        │               │                                                              │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ gpgv                      │ CVE-2022-3219       │          │              │ 2.2.40-1.1             │               │ gnupg: denial of service issue (resource consumption) using  │
│                           │                     │          │              │                        │               │ compressed packets                                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-3219                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-30258      │          │              │                        │               │ gnupg: verification DoS due to a malicious subkey in the     │
│                           │                     │          │              │                        │               │ keyring                                                      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-30258                   │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libapt-pkg6.0             │ CVE-2011-3374       │          │              │ 2.6.1                  │               │ It was found that apt-key in apt, all versions, do not       │
│                           │                     │          │              │                        │               │ correctly...                                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2011-3374                    │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libasan8                  │ CVE-2022-27943      │          │              │ 12.2.0-14+deb12u1      │               │ binutils: libiberty/rust-demangle.c in GNU GCC 11.2 allows   │
│                           │                     │          │              │                        │               │ stack exhaustion in demangle_const                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-27943                   │
├───────────────────────────┤                     │          │              │                        ├───────────────┤                                                              │
│ libatomic1                │                     │          │              │                        │               │                                                              │
│                           │                     │          │              │                        │               │                                                              │
│                           │                     │          │              │                        │               │                                                              │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libbinutils               │ CVE-2017-13716      │          │              │ 2.40-2                 │               │ binutils: Memory leak with the C++ symbol demangler routine  │
│                           │                     │          │              │                        │               │ in libiberty                                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2017-13716                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20673      │          │              │                        │               │ libiberty: Integer overflow in demangle_template() function  │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-20673                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20712      │          │              │                        │               │ libiberty: heap-based buffer over-read in d_expression_1     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-20712                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-9996       │          │              │                        │               │ binutils: Stack-overflow in libiberty/cplus-dem.c causes     │
│                           │                     │          │              │                        │               │ crash                                                        │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-9996                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2021-32256      │          │              │                        │               │ binutils: stack-overflow issue in demangle_type in           │
│                           │                     │          │              │                        │               │ rust-demangle.c.                                             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2021-32256                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2023-1972       │          │              │                        │               │ binutils: Illegal memory access when accessing a             │
│                           │                     │          │              │                        │               │ zer0-lengthverdef table                                      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-1972                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-53589      │          │              │                        │               │ binutils: objdump: buffer Overflow in the BFD library's      │
│                           │                     │          │              │                        │               │ handling of tekhex format...                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-53589                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-57360      │          │              │                        │               │ binutils: nm: potential segmentation fault when displaying   │
│                           │                     │          │              │                        │               │ symbols without version info                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-57360                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-0840       │          │              │                        │               │ binutils: GNU Binutils objdump.c disassemble_bytes           │
│                           │                     │          │              │                        │               │ stack-based overflow                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-0840                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1147       │          │              │                        │               │ binutils: GNU Binutils nm nm.c internal_strlen buffer        │
│                           │                     │          │              │                        │               │ overflow                                                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1147                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1148       │          │              │                        │               │ binutils: GNU Binutils ld ldelfgen.c link_order_scan memory  │
│                           │                     │          │              │                        │               │ leak                                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1148                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1149       │          │              │                        │               │ binutils: GNU Binutils ld xmalloc.c xstrdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1149                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1150       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_malloc memory leak    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1150                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1151       │          │              │                        │               │ binutils: GNU Binutils ld xmemdup.c xmemdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1151                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1152       │          │              │                        │               │ binutils: GNU Binutils ld xstrdup.c xstrdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1152                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1153       │          │              │                        │               │ binutils: GNU Binutils format.c bfd_set_format memory        │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1153                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1176       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │              │                        │               │ heap-based overflow                                          │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1176                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1178       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1178                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1179       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1179                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1180       │          │              │                        │               │ binutils: GNU Binutils ld elf-eh-frame.c                     │
│                           │                     │          │              │                        │               │ _bfd_elf_write_section_eh_frame memory corruption            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1180                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1181       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │              │                        │               │ memory corruption                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1181                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1182       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c                          │
│                           │                     │          │              │                        │               │ bfd_elf_reloc_symbol_deleted_p memory corruption             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1182                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-3198       │          │              │                        │               │ binutils: GNU Binutils objdump bucomm.c display_info memory  │
│                           │                     │          │              │                        │               │ leak                                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-3198                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5244       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c elf_gc_sweep memory      │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-5244                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5245       │          │              │                        │               │ binutils: GNU Binutils objdump debug.c debug_type_samep      │
│                           │                     │          │              │                        │               │ memory corruption                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-5245                    │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libblkid1                 │ CVE-2022-0563       │          │              │ 2.38.1-5+deb12u3       │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                           │                     │          │              │                        │               │ and chsh when compiled...                                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├───────────────────────────┼─────────────────────┼──────────┤              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libc-bin                  │ CVE-2025-4802       │ HIGH     │              │ 2.36-9+deb12u10        │               │ glibc: static setuid binary dlopen may incorrectly search    │
│                           │                     │          │              │                        │               │ LD_LIBRARY_PATH                                              │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-4802                    │
│                           ├─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2010-4756       │ LOW      │              │                        │               │ glibc: glob implementation can cause excessive CPU and       │
│                           │                     │          │              │                        │               │ memory consumption due to...                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2010-4756                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20796      │          │              │                        │               │ glibc: uncontrolled recursion in function                    │
│                           │                     │          │              │                        │               │ check_dst_limits_calc_pos_1 in posix/regexec.c               │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-20796                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2019-1010022    │          │              │                        │               │ glibc: stack guard protection bypass                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2019-1010022                 │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2019-1010023    │          │              │                        │               │ glibc: running ldd on malicious ELF leads to code execution  │
│                           │                     │          │              │                        │               │ because of...                                                │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2019-1010023                 │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2019-1010024    │          │              │                        │               │ glibc: ASLR bypass using cache of thread stack and heap      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2019-1010024                 │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2019-1010025    │          │              │                        │               │ glibc: information disclosure of heap addresses of           │
│                           │                     │          │              │                        │               │ pthread_created thread                                       │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2019-1010025                 │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2019-9192       │          │              │                        │               │ glibc: uncontrolled recursion in function                    │
│                           │                     │          │              │                        │               │ check_dst_limits_calc_pos_1 in posix/regexec.c               │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2019-9192                    │
├───────────────────────────┼─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│ libc6                     │ CVE-2025-4802       │ HIGH     │              │                        │               │ glibc: static setuid binary dlopen may incorrectly search    │
│                           │                     │          │              │                        │               │ LD_LIBRARY_PATH                                              │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-4802                    │
│                           ├─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2010-4756       │ LOW      │              │                        │               │ glibc: glob implementation can cause excessive CPU and       │
│                           │                     │          │              │                        │               │ memory consumption due to...                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2010-4756                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20796      │          │              │                        │               │ glibc: uncontrolled recursion in function                    │
│                           │                     │          │              │                        │               │ check_dst_limits_calc_pos_1 in posix/regexec.c               │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-20796                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2019-1010022    │          │              │                        │               │ glibc: stack guard protection bypass                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2019-1010022                 │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2019-1010023    │          │              │                        │               │ glibc: running ldd on malicious ELF leads to code execution  │
│                           │                     │          │              │                        │               │ because of...                                                │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2019-1010023                 │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2019-1010024    │          │              │                        │               │ glibc: ASLR bypass using cache of thread stack and heap      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2019-1010024                 │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2019-1010025    │          │              │                        │               │ glibc: information disclosure of heap addresses of           │
│                           │                     │          │              │                        │               │ pthread_created thread                                       │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2019-1010025                 │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2019-9192       │          │              │                        │               │ glibc: uncontrolled recursion in function                    │
│                           │                     │          │              │                        │               │ check_dst_limits_calc_pos_1 in posix/regexec.c               │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2019-9192                    │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libcc1-0                  │ CVE-2022-27943      │          │              │ 12.2.0-14+deb12u1      │               │ binutils: libiberty/rust-demangle.c in GNU GCC 11.2 allows   │
│                           │                     │          │              │                        │               │ stack exhaustion in demangle_const                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-27943                   │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libctf-nobfd0             │ CVE-2017-13716      │          │              │ 2.40-2                 │               │ binutils: Memory leak with the C++ symbol demangler routine  │
│                           │                     │          │              │                        │               │ in libiberty                                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2017-13716                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20673      │          │              │                        │               │ libiberty: Integer overflow in demangle_template() function  │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-20673                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20712      │          │              │                        │               │ libiberty: heap-based buffer over-read in d_expression_1     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-20712                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-9996       │          │              │                        │               │ binutils: Stack-overflow in libiberty/cplus-dem.c causes     │
│                           │                     │          │              │                        │               │ crash                                                        │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-9996                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2021-32256      │          │              │                        │               │ binutils: stack-overflow issue in demangle_type in           │
│                           │                     │          │              │                        │               │ rust-demangle.c.                                             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2021-32256                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2023-1972       │          │              │                        │               │ binutils: Illegal memory access when accessing a             │
│                           │                     │          │              │                        │               │ zer0-lengthverdef table                                      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-1972                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-53589      │          │              │                        │               │ binutils: objdump: buffer Overflow in the BFD library's      │
│                           │                     │          │              │                        │               │ handling of tekhex format...                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-53589                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-57360      │          │              │                        │               │ binutils: nm: potential segmentation fault when displaying   │
│                           │                     │          │              │                        │               │ symbols without version info                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-57360                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-0840       │          │              │                        │               │ binutils: GNU Binutils objdump.c disassemble_bytes           │
│                           │                     │          │              │                        │               │ stack-based overflow                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-0840                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1147       │          │              │                        │               │ binutils: GNU Binutils nm nm.c internal_strlen buffer        │
│                           │                     │          │              │                        │               │ overflow                                                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1147                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1148       │          │              │                        │               │ binutils: GNU Binutils ld ldelfgen.c link_order_scan memory  │
│                           │                     │          │              │                        │               │ leak                                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1148                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1149       │          │              │                        │               │ binutils: GNU Binutils ld xmalloc.c xstrdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1149                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1150       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_malloc memory leak    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1150                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1151       │          │              │                        │               │ binutils: GNU Binutils ld xmemdup.c xmemdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1151                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1152       │          │              │                        │               │ binutils: GNU Binutils ld xstrdup.c xstrdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1152                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1153       │          │              │                        │               │ binutils: GNU Binutils format.c bfd_set_format memory        │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1153                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1176       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │              │                        │               │ heap-based overflow                                          │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1176                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1178       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1178                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1179       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1179                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1180       │          │              │                        │               │ binutils: GNU Binutils ld elf-eh-frame.c                     │
│                           │                     │          │              │                        │               │ _bfd_elf_write_section_eh_frame memory corruption            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1180                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1181       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │              │                        │               │ memory corruption                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1181                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1182       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c                          │
│                           │                     │          │              │                        │               │ bfd_elf_reloc_symbol_deleted_p memory corruption             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1182                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-3198       │          │              │                        │               │ binutils: GNU Binutils objdump bucomm.c display_info memory  │
│                           │                     │          │              │                        │               │ leak                                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-3198                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5244       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c elf_gc_sweep memory      │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-5244                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5245       │          │              │                        │               │ binutils: GNU Binutils objdump debug.c debug_type_samep      │
│                           │                     │          │              │                        │               │ memory corruption                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-5245                    │
├───────────────────────────┼─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│ libctf0                   │ CVE-2017-13716      │          │              │                        │               │ binutils: Memory leak with the C++ symbol demangler routine  │
│                           │                     │          │              │                        │               │ in libiberty                                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2017-13716                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20673      │          │              │                        │               │ libiberty: Integer overflow in demangle_template() function  │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-20673                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20712      │          │              │                        │               │ libiberty: heap-based buffer over-read in d_expression_1     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-20712                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-9996       │          │              │                        │               │ binutils: Stack-overflow in libiberty/cplus-dem.c causes     │
│                           │                     │          │              │                        │               │ crash                                                        │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-9996                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2021-32256      │          │              │                        │               │ binutils: stack-overflow issue in demangle_type in           │
│                           │                     │          │              │                        │               │ rust-demangle.c.                                             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2021-32256                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2023-1972       │          │              │                        │               │ binutils: Illegal memory access when accessing a             │
│                           │                     │          │              │                        │               │ zer0-lengthverdef table                                      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-1972                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-53589      │          │              │                        │               │ binutils: objdump: buffer Overflow in the BFD library's      │
│                           │                     │          │              │                        │               │ handling of tekhex format...                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-53589                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-57360      │          │              │                        │               │ binutils: nm: potential segmentation fault when displaying   │
│                           │                     │          │              │                        │               │ symbols without version info                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-57360                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-0840       │          │              │                        │               │ binutils: GNU Binutils objdump.c disassemble_bytes           │
│                           │                     │          │              │                        │               │ stack-based overflow                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-0840                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1147       │          │              │                        │               │ binutils: GNU Binutils nm nm.c internal_strlen buffer        │
│                           │                     │          │              │                        │               │ overflow                                                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1147                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1148       │          │              │                        │               │ binutils: GNU Binutils ld ldelfgen.c link_order_scan memory  │
│                           │                     │          │              │                        │               │ leak                                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1148                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1149       │          │              │                        │               │ binutils: GNU Binutils ld xmalloc.c xstrdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1149                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1150       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_malloc memory leak    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1150                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1151       │          │              │                        │               │ binutils: GNU Binutils ld xmemdup.c xmemdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1151                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1152       │          │              │                        │               │ binutils: GNU Binutils ld xstrdup.c xstrdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1152                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1153       │          │              │                        │               │ binutils: GNU Binutils format.c bfd_set_format memory        │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1153                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1176       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │              │                        │               │ heap-based overflow                                          │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1176                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1178       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1178                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1179       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1179                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1180       │          │              │                        │               │ binutils: GNU Binutils ld elf-eh-frame.c                     │
│                           │                     │          │              │                        │               │ _bfd_elf_write_section_eh_frame memory corruption            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1180                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1181       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │              │                        │               │ memory corruption                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1181                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1182       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c                          │
│                           │                     │          │              │                        │               │ bfd_elf_reloc_symbol_deleted_p memory corruption             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1182                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-3198       │          │              │                        │               │ binutils: GNU Binutils objdump bucomm.c display_info memory  │
│                           │                     │          │              │                        │               │ leak                                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-3198                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5244       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c elf_gc_sweep memory      │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-5244                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5245       │          │              │                        │               │ binutils: GNU Binutils objdump debug.c debug_type_samep      │
│                           │                     │          │              │                        │               │ memory corruption                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-5245                    │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libcurl4                  │ CVE-2024-2379       │          │              │ 7.88.1-10+deb12u12     │               │ curl: QUIC certificate check bypass with wolfSSL             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-2379                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-0725       │          │              │                        │               │ libcurl: Buffer Overflow in libcurl via zlib Integer         │
│                           │                     │          │              │                        │               │ Overflow                                                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-0725                    │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libgcc-12-dev             │ CVE-2022-27943      │          │              │ 12.2.0-14+deb12u1      │               │ binutils: libiberty/rust-demangle.c in GNU GCC 11.2 allows   │
│                           │                     │          │              │                        │               │ stack exhaustion in demangle_const                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-27943                   │
├───────────────────────────┤                     │          │              │                        ├───────────────┤                                                              │
│ libgcc-s1                 │                     │          │              │                        │               │                                                              │
│                           │                     │          │              │                        │               │                                                              │
│                           │                     │          │              │                        │               │                                                              │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libgcrypt20               │ CVE-2018-6829       │          │              │ 1.10.1-3               │               │ libgcrypt: ElGamal implementation doesn't have semantic      │
│                           │                     │          │              │                        │               │ security due to incorrectly encoded plaintexts...            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-6829                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-2236       │          │              │                        │               │ libgcrypt: vulnerable to Marvin Attack                       │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-2236                    │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libgnutls30               │ CVE-2011-3389       │          │              │ 3.7.9-2+deb12u4        │               │ HTTPS: block-wise chosen-plaintext attack against SSL/TLS    │
│                           │                     │          │              │                        │               │ (BEAST)                                                      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2011-3389                    │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libgomp1                  │ CVE-2022-27943      │          │              │ 12.2.0-14+deb12u1      │               │ binutils: libiberty/rust-demangle.c in GNU GCC 11.2 allows   │
│                           │                     │          │              │                        │               │ stack exhaustion in demangle_const                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-27943                   │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libgprofng0               │ CVE-2017-13716      │          │              │ 2.40-2                 │               │ binutils: Memory leak with the C++ symbol demangler routine  │
│                           │                     │          │              │                        │               │ in libiberty                                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2017-13716                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20673      │          │              │                        │               │ libiberty: Integer overflow in demangle_template() function  │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-20673                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20712      │          │              │                        │               │ libiberty: heap-based buffer over-read in d_expression_1     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-20712                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-9996       │          │              │                        │               │ binutils: Stack-overflow in libiberty/cplus-dem.c causes     │
│                           │                     │          │              │                        │               │ crash                                                        │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-9996                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2021-32256      │          │              │                        │               │ binutils: stack-overflow issue in demangle_type in           │
│                           │                     │          │              │                        │               │ rust-demangle.c.                                             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2021-32256                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2023-1972       │          │              │                        │               │ binutils: Illegal memory access when accessing a             │
│                           │                     │          │              │                        │               │ zer0-lengthverdef table                                      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-1972                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-53589      │          │              │                        │               │ binutils: objdump: buffer Overflow in the BFD library's      │
│                           │                     │          │              │                        │               │ handling of tekhex format...                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-53589                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-57360      │          │              │                        │               │ binutils: nm: potential segmentation fault when displaying   │
│                           │                     │          │              │                        │               │ symbols without version info                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-57360                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-0840       │          │              │                        │               │ binutils: GNU Binutils objdump.c disassemble_bytes           │
│                           │                     │          │              │                        │               │ stack-based overflow                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-0840                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1147       │          │              │                        │               │ binutils: GNU Binutils nm nm.c internal_strlen buffer        │
│                           │                     │          │              │                        │               │ overflow                                                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1147                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1148       │          │              │                        │               │ binutils: GNU Binutils ld ldelfgen.c link_order_scan memory  │
│                           │                     │          │              │                        │               │ leak                                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1148                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1149       │          │              │                        │               │ binutils: GNU Binutils ld xmalloc.c xstrdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1149                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1150       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_malloc memory leak    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1150                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1151       │          │              │                        │               │ binutils: GNU Binutils ld xmemdup.c xmemdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1151                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1152       │          │              │                        │               │ binutils: GNU Binutils ld xstrdup.c xstrdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1152                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1153       │          │              │                        │               │ binutils: GNU Binutils format.c bfd_set_format memory        │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1153                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1176       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │              │                        │               │ heap-based overflow                                          │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1176                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1178       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1178                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1179       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1179                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1180       │          │              │                        │               │ binutils: GNU Binutils ld elf-eh-frame.c                     │
│                           │                     │          │              │                        │               │ _bfd_elf_write_section_eh_frame memory corruption            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1180                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1181       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │              │                        │               │ memory corruption                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1181                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1182       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c                          │
│                           │                     │          │              │                        │               │ bfd_elf_reloc_symbol_deleted_p memory corruption             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1182                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-3198       │          │              │                        │               │ binutils: GNU Binutils objdump bucomm.c display_info memory  │
│                           │                     │          │              │                        │               │ leak                                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-3198                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5244       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c elf_gc_sweep memory      │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-5244                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5245       │          │              │                        │               │ binutils: GNU Binutils objdump debug.c debug_type_samep      │
│                           │                     │          │              │                        │               │ memory corruption                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-5245                    │
├───────────────────────────┼─────────────────────┼──────────┤              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libgssapi-krb5-2          │ CVE-2025-3576       │ MEDIUM   │              │ 1.20.1-2+deb12u3       │               │ krb5: Kerberos RC4-HMAC-MD5 Checksum Vulnerability Enabling  │
│                           │                     │          │              │                        │               │ Message Spoofing via MD5 Collisions                          │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-3576                    │
│                           ├─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-5709       │ LOW      │              │                        │               │ krb5: integer overflow in dbentry->n_key_data in             │
│                           │                     │          │              │                        │               │ kadmin/dbutil/dump.c                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-5709                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-26458      │          │              │                        │               │ krb5: Memory leak at /krb5/src/lib/rpc/pmap_rmt.c            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-26458                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-26461      │          │              │                        │               │ krb5: Memory leak at /krb5/src/lib/gssapi/krb5/k5sealv3.c    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-26461                   │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libitm1                   │ CVE-2022-27943      │          │              │ 12.2.0-14+deb12u1      │               │ binutils: libiberty/rust-demangle.c in GNU GCC 11.2 allows   │
│                           │                     │          │              │                        │               │ stack exhaustion in demangle_const                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-27943                   │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libjansson4               │ CVE-2020-36325      │          │              │ 2.14-2                 │               │ jansson: out-of-bounds read in json_loads() due to a parsing │
│                           │                     │          │              │                        │               │ error                                                        │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2020-36325                   │
├───────────────────────────┼─────────────────────┼──────────┤              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libk5crypto3              │ CVE-2025-3576       │ MEDIUM   │              │ 1.20.1-2+deb12u3       │               │ krb5: Kerberos RC4-HMAC-MD5 Checksum Vulnerability Enabling  │
│                           │                     │          │              │                        │               │ Message Spoofing via MD5 Collisions                          │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-3576                    │
│                           ├─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-5709       │ LOW      │              │                        │               │ krb5: integer overflow in dbentry->n_key_data in             │
│                           │                     │          │              │                        │               │ kadmin/dbutil/dump.c                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-5709                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-26458      │          │              │                        │               │ krb5: Memory leak at /krb5/src/lib/rpc/pmap_rmt.c            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-26458                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-26461      │          │              │                        │               │ krb5: Memory leak at /krb5/src/lib/gssapi/krb5/k5sealv3.c    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-26461                   │
├───────────────────────────┼─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│ libkrb5-3                 │ CVE-2025-3576       │ MEDIUM   │              │                        │               │ krb5: Kerberos RC4-HMAC-MD5 Checksum Vulnerability Enabling  │
│                           │                     │          │              │                        │               │ Message Spoofing via MD5 Collisions                          │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-3576                    │
│                           ├─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-5709       │ LOW      │              │                        │               │ krb5: integer overflow in dbentry->n_key_data in             │
│                           │                     │          │              │                        │               │ kadmin/dbutil/dump.c                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-5709                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-26458      │          │              │                        │               │ krb5: Memory leak at /krb5/src/lib/rpc/pmap_rmt.c            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-26458                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-26461      │          │              │                        │               │ krb5: Memory leak at /krb5/src/lib/gssapi/krb5/k5sealv3.c    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-26461                   │
├───────────────────────────┼─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│ libkrb5support0           │ CVE-2025-3576       │ MEDIUM   │              │                        │               │ krb5: Kerberos RC4-HMAC-MD5 Checksum Vulnerability Enabling  │
│                           │                     │          │              │                        │               │ Message Spoofing via MD5 Collisions                          │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-3576                    │
│                           ├─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-5709       │ LOW      │              │                        │               │ krb5: integer overflow in dbentry->n_key_data in             │
│                           │                     │          │              │                        │               │ kadmin/dbutil/dump.c                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-5709                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-26458      │          │              │                        │               │ krb5: Memory leak at /krb5/src/lib/rpc/pmap_rmt.c            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-26458                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-26461      │          │              │                        │               │ krb5: Memory leak at /krb5/src/lib/gssapi/krb5/k5sealv3.c    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-26461                   │
├───────────────────────────┼─────────────────────┼──────────┤              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libldap-2.5-0             │ CVE-2023-2953       │ HIGH     │              │ 2.5.13+dfsg-5          │               │ openldap: null pointer dereference in ber_memalloc_x         │
│                           │                     │          │              │                        │               │ function                                                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-2953                    │
│                           ├─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2015-3276       │ LOW      │              │                        │               │ openldap: incorrect multi-keyword mode cipherstring parsing  │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2015-3276                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2017-14159      │          │              │                        │               │ openldap: Privilege escalation via PID file manipulation     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2017-14159                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2017-17740      │          │              │                        │               │ openldap: contrib/slapd-modules/nops/nops.c attempts to free │
│                           │                     │          │              │                        │               │ stack buffer allowing remote attackers to cause...           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2017-17740                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2020-15719      │          │              │                        │               │ openldap: Certificate validation incorrectly matches name    │
│                           │                     │          │              │                        │               │ against CN-ID                                                │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2020-15719                   │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ liblsan0                  │ CVE-2022-27943      │          │              │ 12.2.0-14+deb12u1      │               │ binutils: libiberty/rust-demangle.c in GNU GCC 11.2 allows   │
│                           │                     │          │              │                        │               │ stack exhaustion in demangle_const                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-27943                   │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libmount1                 │ CVE-2022-0563       │          │              │ 2.38.1-5+deb12u3       │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                           │                     │          │              │                        │               │ and chsh when compiled...                                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├───────────────────────────┼─────────────────────┼──────────┤              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libncursesw6              │ CVE-2023-50495      │ MEDIUM   │              │ 6.4-4                  │               │ ncurses: segmentation fault via _nc_wrap_entry()             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-50495                   │
│                           ├─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-6141       │ LOW      │              │                        │               │ gnu-ncurses: ncurses Stack Buffer Overflow                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-6141                    │
├───────────────────────────┼─────────────────────┼──────────┤              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libpam-modules            │ CVE-2025-6020       │ HIGH     │              │ 1.5.2-6+deb12u1        │               │ linux-pam: Linux-pam directory Traversal                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-6020                    │
│                           ├─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-10041      │ MEDIUM   │              │                        │               │ pam: libpam: Libpam vulnerable to read hashed password       │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-10041                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-22365      │          │              │                        │               │ pam: allowing unprivileged user to block another user        │
│                           │                     │          │              │                        │               │ namespace                                                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-22365                   │
├───────────────────────────┼─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│ libpam-modules-bin        │ CVE-2025-6020       │ HIGH     │              │                        │               │ linux-pam: Linux-pam directory Traversal                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-6020                    │
│                           ├─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-10041      │ MEDIUM   │              │                        │               │ pam: libpam: Libpam vulnerable to read hashed password       │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-10041                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-22365      │          │              │                        │               │ pam: allowing unprivileged user to block another user        │
│                           │                     │          │              │                        │               │ namespace                                                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-22365                   │
├───────────────────────────┼─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│ libpam-runtime            │ CVE-2025-6020       │ HIGH     │              │                        │               │ linux-pam: Linux-pam directory Traversal                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-6020                    │
│                           ├─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-10041      │ MEDIUM   │              │                        │               │ pam: libpam: Libpam vulnerable to read hashed password       │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-10041                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-22365      │          │              │                        │               │ pam: allowing unprivileged user to block another user        │
│                           │                     │          │              │                        │               │ namespace                                                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-22365                   │
├───────────────────────────┼─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│ libpam0g                  │ CVE-2025-6020       │ HIGH     │              │                        │               │ linux-pam: Linux-pam directory Traversal                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-6020                    │
│                           ├─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-10041      │ MEDIUM   │              │                        │               │ pam: libpam: Libpam vulnerable to read hashed password       │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-10041                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-22365      │          │              │                        │               │ pam: allowing unprivileged user to block another user        │
│                           │                     │          │              │                        │               │ namespace                                                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-22365                   │
├───────────────────────────┼─────────────────────┼──────────┤              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libquadmath0              │ CVE-2022-27943      │ LOW      │              │ 12.2.0-14+deb12u1      │               │ binutils: libiberty/rust-demangle.c in GNU GCC 11.2 allows   │
│                           │                     │          │              │                        │               │ stack exhaustion in demangle_const                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-27943                   │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libsmartcols1             │ CVE-2022-0563       │          │              │ 2.38.1-5+deb12u3       │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                           │                     │          │              │                        │               │ and chsh when compiled...                                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├───────────────────────────┼─────────────────────┼──────────┤              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libsqlite3-0              │ CVE-2025-29088      │ MEDIUM   │              │ 3.40.1-2+deb12u1       │               │ sqlite: Denial of Service in SQLite                          │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-29088                   │
│                           ├─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2021-45346      │ LOW      │              │                        │               │ sqlite: crafted SQL query allows a malicious user to obtain  │
│                           │                     │          │              │                        │               │ sensitive information...                                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2021-45346                   │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libssl3                   │ CVE-2025-27587      │          │              │ 3.0.16-1~deb12u1       │               │ OpenSSL 3.0.0 through 3.3.2 on the PowerPC architecture is   │
│                           │                     │          │              │                        │               │ vulnerable ......                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-27587                   │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libstdc++6                │ CVE-2022-27943      │          │              │ 12.2.0-14+deb12u1      │               │ binutils: libiberty/rust-demangle.c in GNU GCC 11.2 allows   │
│                           │                     │          │              │                        │               │ stack exhaustion in demangle_const                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-27943                   │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libsystemd0               │ CVE-2013-4392       │          │              │ 252.38-1~deb12u1       │               │ systemd: TOCTOU race condition when updating file            │
│                           │                     │          │              │                        │               │ permissions and SELinux security contexts...                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2013-4392                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2023-31437      │          │              │                        │               │ An issue was discovered in systemd 253. An attacker can      │
│                           │                     │          │              │                        │               │ modify a...                                                  │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-31437                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2023-31438      │          │              │                        │               │ An issue was discovered in systemd 253. An attacker can      │
│                           │                     │          │              │                        │               │ truncate a...                                                │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-31438                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2023-31439      │          │              │                        │               │ An issue was discovered in systemd 253. An attacker can      │
│                           │                     │          │              │                        │               │ modify the...                                                │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-31439                   │
├───────────────────────────┼─────────────────────┼──────────┤              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libtinfo6                 │ CVE-2023-50495      │ MEDIUM   │              │ 6.4-4                  │               │ ncurses: segmentation fault via _nc_wrap_entry()             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-50495                   │
│                           ├─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-6141       │ LOW      │              │                        │               │ gnu-ncurses: ncurses Stack Buffer Overflow                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-6141                    │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libtsan2                  │ CVE-2022-27943      │          │              │ 12.2.0-14+deb12u1      │               │ binutils: libiberty/rust-demangle.c in GNU GCC 11.2 allows   │
│                           │                     │          │              │                        │               │ stack exhaustion in demangle_const                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-27943                   │
├───────────────────────────┤                     │          │              │                        ├───────────────┤                                                              │
│ libubsan1                 │                     │          │              │                        │               │                                                              │
│                           │                     │          │              │                        │               │                                                              │
│                           │                     │          │              │                        │               │                                                              │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libudev1                  │ CVE-2013-4392       │          │              │ 252.38-1~deb12u1       │               │ systemd: TOCTOU race condition when updating file            │
│                           │                     │          │              │                        │               │ permissions and SELinux security contexts...                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2013-4392                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2023-31437      │          │              │                        │               │ An issue was discovered in systemd 253. An attacker can      │
│                           │                     │          │              │                        │               │ modify a...                                                  │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-31437                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2023-31438      │          │              │                        │               │ An issue was discovered in systemd 253. An attacker can      │
│                           │                     │          │              │                        │               │ truncate a...                                                │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-31438                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2023-31439      │          │              │                        │               │ An issue was discovered in systemd 253. An attacker can      │
│                           │                     │          │              │                        │               │ modify the...                                                │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-31439                   │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libuuid1                  │ CVE-2022-0563       │          │              │ 2.38.1-5+deb12u3       │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                           │                     │          │              │                        │               │ and chsh when compiled...                                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ login                     │ CVE-2007-5686       │          │              │ 1:4.13+dfsg1-1+deb12u1 │               │ initscripts in rPath Linux 1 sets insecure permissions for   │
│                           │                     │          │              │                        │               │ the /var/lo ......                                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2007-5686                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-56433      │          │              │                        │               │ shadow-utils: Default subordinate ID configuration in        │
│                           │                     │          │              │                        │               │ /etc/login.defs could lead to compromise                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-56433                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ TEMP-0628843-DBAD28 │          │              │                        │               │ [more related to CVE-2005-4890]                              │
│                           │                     │          │              │                        │               │ https://security-tracker.debian.org/tracker/TEMP-0628843-DB- │
│                           │                     │          │              │                        │               │ AD28                                                         │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ mount                     │ CVE-2022-0563       │          │              │ 2.38.1-5+deb12u3       │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                           │                     │          │              │                        │               │ and chsh when compiled...                                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├───────────────────────────┼─────────────────────┼──────────┤              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ ncurses-base              │ CVE-2023-50495      │ MEDIUM   │              │ 6.4-4                  │               │ ncurses: segmentation fault via _nc_wrap_entry()             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-50495                   │
│                           ├─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-6141       │ LOW      │              │                        │               │ gnu-ncurses: ncurses Stack Buffer Overflow                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-6141                    │
├───────────────────────────┼─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│ ncurses-bin               │ CVE-2023-50495      │ MEDIUM   │              │                        │               │ ncurses: segmentation fault via _nc_wrap_entry()             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-50495                   │
│                           ├─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-6141       │ LOW      │              │                        │               │ gnu-ncurses: ncurses Stack Buffer Overflow                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-6141                    │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ openssl                   │ CVE-2025-27587      │          │              │ 3.0.16-1~deb12u1       │               │ OpenSSL 3.0.0 through 3.3.2 on the PowerPC architecture is   │
│                           │                     │          │              │                        │               │ vulnerable ......                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-27587                   │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ passwd                    │ CVE-2007-5686       │          │              │ 1:4.13+dfsg1-1+deb12u1 │               │ initscripts in rPath Linux 1 sets insecure permissions for   │
│                           │                     │          │              │                        │               │ the /var/lo ......                                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2007-5686                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-56433      │          │              │                        │               │ shadow-utils: Default subordinate ID configuration in        │
│                           │                     │          │              │                        │               │ /etc/login.defs could lead to compromise                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-56433                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ TEMP-0628843-DBAD28 │          │              │                        │               │ [more related to CVE-2005-4890]                              │
│                           │                     │          │              │                        │               │ https://security-tracker.debian.org/tracker/TEMP-0628843-DB- │
│                           │                     │          │              │                        │               │ AD28                                                         │
├───────────────────────────┼─────────────────────┼──────────┤              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ perl-base                 │ CVE-2023-31484      │ HIGH     │              │ 5.36.0-7+deb12u2       │               │ perl: CPAN.pm does not verify TLS certificates when          │
│                           │                     │          │              │                        │               │ downloading distributions over HTTPS...                      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-31484                   │
│                           ├─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-40909      │ MEDIUM   │              │                        │               │ perl: Perl threads have a working directory race condition   │
│                           │                     │          │              │                        │               │ where file operations...                                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-40909                   │
│                           ├─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2011-4116       │ LOW      │              │                        │               │ perl: File:: Temp insecure temporary file handling           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2011-4116                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2023-31486      │          │              │                        │               │ http-tiny: insecure TLS cert default                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-31486                   │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ sysvinit-utils            │ TEMP-0517018-A83CE6 │          │              │ 3.06-4                 │               │ [sysvinit: no-root option in expert installer exposes        │
│                           │                     │          │              │                        │               │ locally exploitable security flaw]                           │
│                           │                     │          │              │                        │               │ https://security-tracker.debian.org/tracker/TEMP-0517018-A8- │
│                           │                     │          │              │                        │               │ 3CE6                                                         │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ tar                       │ CVE-2005-2541       │          │              │ 1.34+dfsg-1.2+deb12u1  │               │ tar: does not properly warn the user when extracting setuid  │
│                           │                     │          │              │                        │               │ or setgid...                                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2005-2541                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ TEMP-0290435-0B57B5 │          │              │                        │               │ [tar's rmt command may have undesired side effects]          │
│                           │                     │          │              │                        │               │ https://security-tracker.debian.org/tracker/TEMP-0290435-0B- │
│                           │                     │          │              │                        │               │ 57B5                                                         │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ util-linux                │ CVE-2022-0563       │          │              │ 2.38.1-5+deb12u3       │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                           │                     │          │              │                        │               │ and chsh when compiled...                                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├───────────────────────────┤                     │          │              │                        ├───────────────┤                                                              │
│ util-linux-extra          │                     │          │              │                        │               │                                                              │
│                           │                     │          │              │                        │               │                                                              │
│                           │                     │          │              │                        │               │                                                              │
├───────────────────────────┼─────────────────────┼──────────┼──────────────┼────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ zlib1g                    │ CVE-2023-45853      │ CRITICAL │ will_not_fix │ 1:1.2.13.dfsg-1        │               │ zlib: integer overflow and resultant heap-based buffer       │
│                           │                     │          │              │                        │               │ overflow in zipOpenNewFileInZip4_6                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-45853                   │
└───────────────────────────┴─────────────────────┴──────────┴──────────────┴────────────────────────┴───────────────┴──────────────────────────────────────────────────────────────┘

Python (python-pkg)
===================
Total: 4 (UNKNOWN: 0, LOW: 0, MEDIUM: 1, HIGH: 3, CRITICAL: 0)

┌───────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬──────────────────────────────────────────────────────────┐
│        Library        │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                          Title                           │
├───────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────┤
│ pip (METADATA)        │ CVE-2023-5752  │ MEDIUM   │ fixed  │ 23.0.1            │ 23.3          │ pip: Mercurial configuration injectable in repo revision │
│                       │                │          │        │                   │               │ when installing via pip                                  │
│                       │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2023-5752                │
├───────────────────────┼────────────────┼──────────┤        ├───────────────────┼───────────────┼──────────────────────────────────────────────────────────┤
│ setuptools (METADATA) │ CVE-2022-40897 │ HIGH     │        │ 58.1.0            │ 65.5.1        │ pypa-setuptools: Regular Expression Denial of Service    │
│                       │                │          │        │                   │               │ (ReDoS) in package_index.py                              │
│                       │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2022-40897               │
│                       ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────┤
│                       │ CVE-2024-6345  │          │        │                   │ 70.0.0        │ pypa/setuptools: Remote code execution via download      │
│                       │                │          │        │                   │               │ functions in the package_index module in...              │
│                       │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2024-6345                │
│                       ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────┤
│                       │ CVE-2025-47273 │          │        │                   │ 78.1.1        │ setuptools: Path Traversal Vulnerability in setuptools   │
│                       │                │          │        │                   │               │ PackageIndex                                             │
│                       │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2025-47273               │
└───────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴──────────────────────────────────────────────────────────┘
```
### Vulnerability Summary

| Image | Critical | High | Medium | Low |
|-------|----------|------|--------|-----|
| Frontend | 0 | 0 | 0 | 0
| Backend | 3 | 11 | 17 | 17
