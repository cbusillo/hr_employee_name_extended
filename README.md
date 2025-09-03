# HR Employee Name Extended

Structured first/last/nickname fields for `hr.employee` with locale-aware formatting and safe inverse writes.

## Features

- First/Last/Nickname fields with chatter tracking
- `name` is compute+inverse (stored), so external writes (imports/API) are parsed back into structured parts
- Locale-aware formatting: western (First Last) or asian (Last First)
- Per-employee override (`name_format`) with optional default from Settings
- Search across `name`, `first_name`, `last_name`, `nick_name`
- No cross-model side effects by default; partner/users sync remains opt-in via context

## Settings (HR)

- Default Name Format: western | asian | custom
- Custom Pattern (when format = custom): `{first_name}`, `{last_name}`, `{nickname}`

Defaults apply only when creating a new employee; runtime compute/inverse always respect the per-employee override.

## Usage

- Set default format in HR Settings
- For employees who need a different order, set `Name Format` on the employee
- Writing `employee.name` as a single token keeps the last name unchanged

## Tests

- Unit tests cover: defaults, per-employee overrides, inverse behavior, and settings impact

