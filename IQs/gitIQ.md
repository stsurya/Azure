## 1. How do you resolve merge conflicts in Git?

Suppose I was working on a feature/login branch and someone changed the same function in the main branch. After running git merge main, I got a conflict in login.js. I resolved it by comparing the business logic changes, testing both versions locally, and merging the appropriate logic, followed by git add and git commit.

## 2. A teammate force-pushed and rewrote history on a shared branch. How do you recover your lost work?

Suppose I pushed commits A → B → C to develop, and my teammate force-pushed their version with only commits A → D. My commits B and C are now missing from the remote. Using git reflog, I find the hash for C, create a new branch from it, verify my changes, and then merge or cherry-pick them back into the shared branch.

## 3. How do you cherry-pick a specific commit from one branch to another?

Sure! Here's an interview-ready explanation for:

---

### 🧠 **Q: How do you cherry-pick a specific commit from one branch to another?**

---

**Answer:**

**Cherry-picking** in Git means picking a specific commit from one branch and applying it onto another branch, without merging the full branch history.

---

### 📌 **Use Case:**

If a developer made a fix on the `develop` branch and I want to apply _just that one commit_ to the `main` branch, cherry-pick is the right choice.

---

### 💻 **Steps to Cherry-pick a Commit:**

1. **Get the commit hash** from the source branch:

   ```
   git log
   ```

2. **Switch to the target branch** where you want to apply the commit:

   ```
   git checkout main
   ```

3. **Cherry-pick the commit:**

   ```
   git cherry-pick <commit-hash>
   ```

   This will apply the exact changes of that commit onto the current branch.

---

### ⚠️ **Handling Conflicts:**

If there's a conflict, Git will pause and ask you to resolve it manually. After resolving:

```
git add .
git cherry-pick --continue
```

---

### 🧪 Example:

> Let’s say there’s a bug fix in commit `abc123` on the `feature/login` branch that needs to go to `main`.
> I’d do:

```
git checkout main
git cherry-pick abc123
```

This brings only that commit’s changes without merging the whole branch.

---

### ✅ Best Practices:

- Cherry-pick only **small, self-contained commits**.
- Avoid cherry-picking merge commits unless you know what you're doing.
- After cherry-picking, run your tests to ensure it works as expected.

---

### ❓ **Q: What is the difference between `git reset`, `git revert`, and `git checkout`?**

---

**Answer:**

These three Git commands serve different purposes in managing commits and working directory changes:

---

### ✅ `git reset`

- **Used to move the HEAD pointer and optionally change the staging area or working directory.**
- It’s mostly used to **undo commits or unstage changes**.

**Example:**

```bash
git reset --soft HEAD~1
```

> This removes the last commit but keeps changes in the staging area.

**Types:**

- `--soft`: Keeps changes staged.
- `--mixed` (default): Keeps changes in the working directory.
- `--hard`: Deletes all changes — be careful!

**⚠️ Not safe on shared branches**, as it rewrites commit history.

---

### ✅ `git revert`

- **Used to undo a commit without modifying history**.
- It creates a **new commit** that reverses the changes from a previous commit.

**Example:**

```bash
git revert <commit-hash>
```

> This is safe for **shared branches** like `main`, because it doesn’t rewrite history.

---

### ✅ `git checkout`

- **Used to switch between branches** or **restore files** to a previous state.

**Examples:**

```bash
git checkout develop           # Switches to another branch
git checkout HEAD~1 app.js     # Restores file from a previous commit
```

Note: In newer Git versions, this is being split into `git switch` (for branches) and `git restore` (for files), but `checkout` still works.

---

### 🧪 Example Scenario:

If I accidentally committed a wrong file:

- I use `git reset` to undo it locally (if not pushed).
- If I already pushed it to a shared branch, I use `git revert` to safely undo it.
- If I just want to get the previous version of a file, I use `git checkout`.

---

### ✅ Summary:

| Command        | Purpose                          | Affects History | Safe for Shared Branches |
| -------------- | -------------------------------- | --------------- | ------------------------ |
| `git reset`    | Undo commits/staging             | ✅ Yes          | ❌ No                    |
| `git revert`   | Create a new commit to undo      | ❌ No           | ✅ Yes                   |
| `git checkout` | Switch branches or restore files | ❌ No           | ✅ Yes                   |

---
