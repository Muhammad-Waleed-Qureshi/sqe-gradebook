# Test Cases

<style>
  table {
    font-size: 13px;
  }
  th, td {
    padding: 6px 8px !important;
  }
</style>

## GradeBook Test Cases

<table>
  <thead>
    <tr>
      <th>TC ID</th>
      <th>Test Case</th>
      <th>Requirement</th>
      <th>Preconditions</th>
      <th>Test Steps</th>
      <th>Expected Result</th>
      <th>Priority</th>
      <th>Type</th>
      <th>Execution Result</th>
      <th>Defect Issue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>TC-001</td>
      <td>Add valid score</td>
      <td>REQ-1</td>
      <td>Student object is created</td>
      <td>Create <code>Student("Ali", 101)</code> and call <code>student.add_score(85)</code>.</td>
      <td>Score <code>85</code> is added successfully.</td>
      <td>High</td>
      <td>Functional / Positive</td>
      <td><strong>FAIL</strong> — <code>Student</code> has no <code>add_score()</code> method.</td>
      <td>#13</td>
    </tr>
    <tr>
      <td>TC-002</td>
      <td>Reject negative score</td>
      <td>REQ-1</td>
      <td>Student object is created</td>
      <td>Create <code>Student("Ali", 101)</code> and call <code>student.add_score(-10)</code>.</td>
      <td>Raises <code>ValueError</code> and scores remain unchanged.</td>
      <td>High</td>
      <td>Negative / Functional</td>
      <td><strong>FAIL</strong> — <code>Student</code> has no <code>add_score()</code> method.</td>
      <td>#13</td>
    </tr>
    <tr>
      <td>TC-003</td>
      <td>Reject non-numeric score</td>
      <td>REQ-1</td>
      <td>Student object is created</td>
      <td>Create <code>Student("Ali", 101)</code> and call <code>student.add_score("abc")</code>.</td>
      <td>Raises <code>TypeError</code> or <code>ValueError</code>.</td>
      <td>Medium</td>
      <td>Negative / Functional</td>
      <td><strong>FAIL</strong> — <code>Student</code> has no <code>add_score()</code> method.</td>
      <td>#13</td>
    </tr>
    <tr>
      <td>TC-004</td>
      <td>Calculate average with scores</td>
      <td>REQ-2</td>
      <td>Student has scores <code>[80, 90, 100]</code></td>
      <td>Set <code>student.scores = [80, 90, 100]</code> and call <code>student.average()</code>.</td>
      <td>Returns correct average <code>90.0</code>.</td>
      <td>High</td>
      <td>Functional</td>
      <td><strong>PASS</strong> — <code>average()</code> returned <code>90</code>.</td>
      <td>—</td>
    </tr>
    <tr>
      <td>TC-005</td>
      <td>Average with empty list</td>
      <td>REQ-2</td>
      <td>Student has an empty scores list <code>[]</code></td>
      <td>Set <code>student.scores = []</code> and call <code>student.average()</code>.</td>
      <td>Returns <code>0.0</code> without crashing.</td>
      <td>High</td>
      <td>Negative / Edge Case</td>
      <td><strong>PASS</strong> — <code>average()</code> returned <code>0</code> without crashing.</td>
      <td>—</td>
    </tr>
    <tr>
      <td>TC-006</td>
      <td>Average with single score</td>
      <td>REQ-2</td>
      <td>Student has a single score <code>[75]</code></td>
      <td>Set <code>student.scores = [75]</code> and call <code>student.average()</code>.</td>
      <td>Returns <code>75.0</code>.</td>
      <td>Medium</td>
      <td>Functional</td>
      <td><strong>PASS</strong> — <code>average()</code> returned <code>75</code>.</td>
      <td>—</td>
    </tr>
    <tr>
      <td>TC-007</td>
      <td>Duplicate roll number rejection</td>
      <td>REQ-3</td>
      <td>GradeBook contains roll number <code>101</code></td>
      <td>Add <code>Student("Ali", 101)</code>, then add <code>Student("Ahmed", 101)</code>.</td>
      <td>Raises <code>ValueError</code> to prevent duplicates.</td>
      <td>High</td>
      <td>Negative / Functional</td>
      <td><strong>PASS</strong> — raised <code>ValueError: Roll number already exists</code>.</td>
      <td>—</td>
    </tr>
    <tr>
      <td>TC-008</td>
      <td>Name case-insensitivity search</td>
      <td>REQ-4</td>
      <td>Student named <code>"Ali"</code> exists</td>
      <td>Add <code>Student("Ali", 101)</code> and search using <code>"ali"</code>.</td>
      <td>System finds and returns the student record.</td>
      <td>Low</td>
      <td>Functional</td>
      <td><strong>FAIL</strong> — <code>GradeBook</code> has no <code>find_student()</code> method.</td>
      <td>#14</td>
    </tr>
    <tr>
      <td>TC-009</td>
      <td>Maximum score boundary (100)</td>
      <td>REQ-5</td>
      <td>Student object is created</td>
      <td>Create <code>Student("Ali", 101)</code> and call <code>student.add_score(100)</code>.</td>
      <td>Score <code>100</code> is accepted successfully.</td>
      <td>Medium</td>
      <td>Boundary</td>
      <td><strong>FAIL</strong> — <code>Student</code> has no <code>add_score()</code> method.</td>
      <td>#13</td>
    </tr>
    <tr>
      <td>TC-010</td>
      <td>Minimum score boundary (0)</td>
      <td>REQ-5</td>
      <td>Student object is created</td>
      <td>Create <code>Student("Ali", 101)</code> and call <code>student.add_score(0)</code>.</td>
      <td>Score <code>0</code> is accepted successfully.</td>
      <td>Medium</td>
      <td>Boundary</td>
      <td><strong>FAIL</strong> — <code>Student</code> has no <code>add_score()</code> method.</td>
      <td>#13</td>
    </tr>
    <tr>
      <td>TC-011</td>
      <td>Grade letter mid-range score</td>
      <td>REQ-6</td>
      <td>Student average is <code>82.0</code></td>
      <td>Set <code>student.scores = [82]</code> and call <code>student.get_grade()</code>.</td>
      <td>Returns grade letter <code>'B'</code>.</td>
      <td>Low</td>
      <td>Functional</td>
      <td><strong>FAIL</strong> — <code>Student</code> has no <code>get_grade()</code> method.</td>
      <td>#15</td>
    </tr>
    <tr>
      <td>TC-012</td>
      <td>Grade letter at exact boundary</td>
      <td>REQ-6</td>
      <td>Student average is exactly <code>90.0</code></td>
      <td>Set <code>student.scores = [90]</code> and call <code>student.get_grade()</code>.</td>
      <td>Returns grade letter <code>'A'</code>.</td>
      <td>Low</td>
      <td>Boundary</td>
      <td><strong>FAIL</strong> — <code>Student</code> has no <code>get_grade()</code> method.</td>
      <td>#15</td>
    </tr>
  </tbody>
</table>

## Execution Summary

<table>
  <thead>
    <tr>
      <th>Status</th>
      <th>Count</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Pass</td><td>3</td></tr>
    <tr><td>Fail</td><td>9</td></tr>
    <tr><td>Blocked</td><td>0</td></tr>
    <tr><td><strong>Total</strong></td><td><strong>12</strong></td></tr>
  </tbody>
</table>

## Defect Summary

<table>
  <thead>
    <tr>
      <th>Defect</th>
      <th>Affected Test Cases</th>
      <th>Defect Issue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Missing <code>Student.add_score()</code> method</td>
      <td>TC-001, TC-002, TC-003, TC-009, TC-010</td>
      <td>#13</td>
    </tr>
    <tr>
      <td>Missing <code>GradeBook.find_student()</code> method</td>
      <td>TC-008</td>
      <td>#14</td>
    </tr>
    <tr>
      <td>Missing <code>Student.get_grade()</code> method</td>
      <td>TC-011, TC-012</td>
      <td>#15</td>
    </tr>
  </tbody>
</table>
